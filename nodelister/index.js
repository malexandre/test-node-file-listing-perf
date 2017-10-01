const list = require('./list')

const test = async() => {
    {
        const hrstart = process.hrtime()
        const res = await list({})
        const hrend = process.hrtime(hrstart)
        console.log(`Simple list: ${hrend[0]}s ${hrend[1] / 1000000}ms for ${res.items.length} items`)
    }

    {
        const hrstart = process.hrtime()
        const res = await list({ filter: 'My Post' })
        const hrend = process.hrtime(hrstart)
        console.log(`Filtered list: ${hrend[0]}s ${hrend[1] / 1000000}ms for ${res.items.length} items`)
    }

    {
        const hrstart = process.hrtime()
        const res = await list({ orderby: 'date' })
        const hrend = process.hrtime(hrstart)
        console.log(`Ordered list: ${hrend[0]}s ${hrend[1] / 1000000}ms for ${res.items.length} items`)
    }

    {
        const hrstart = process.hrtime()
        const res = await list({ orderby: 'date', offset: 50, count: 50 })
        const hrend = process.hrtime(hrstart)
        console.log(`Big list: ${hrend[0]}s ${hrend[1] / 1000000}ms for ${res.items.length} items`)
    }
}

test()
