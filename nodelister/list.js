const _ = require('lodash')
const fs = require('fs-extra')
const frontMatter = require('front-matter')
const moment = require('moment')
const slugify = require('slugify')

const postFolder = 'content/post'

const searchInTitle = (title, search) => {
    title = slugify((title || '').toLowerCase())
    search = slugify((search || '').toLowerCase())

    return title.includes(search)
}

const list = async(options = {}) => {
    options = Object.assign(
        {
            filter: undefined,
            orderby: ['-date'],
            offset: 0,
            count: 10
        },
        options
    )

    if (!Array.isArray(options.orderby)) {
        options.orderby = [options.orderby]
    }

    const found = []

    let files = []
    try {
        files = await fs.readdir(postFolder)
    }
    catch (e) {
        console.log('Post.list: Error listing files from folder', e)
        throw e
    }

    files.forEach(async(file) => {
        let data
        try {
            data = fs.readFileSync(`${postFolder}/${file}`, 'utf8')
        }
        catch (e) {
            console.log('Post.list: Error while reading file', e)
            return
        }
        const attributes = frontMatter(data).attributes
        if (attributes.title && (!options.filter || searchInTitle(attributes.title, options.filter))) {
            found.push({
                path: `${postFolder}/${file}`,
                title: attributes.title,
                date: moment(attributes.date).valueOf(),
                categories: attributes.categories
            })
        }
    })

    const ordered = _.orderBy(
        found,
        options.orderby.map((item) => item.replace(/^-/, '')),
        options.orderby.map((item) => (item[0] === '-' ? 'desc' : 'asc'))
    )

    return {
        items: ordered.slice(options.offset, options.offset + options.count),
        more: ordered.slice(options.offset, options.offset + options.count + 1).length > options.count
    }
}

module.exports = list
