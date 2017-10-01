import os
from datetime import datetime
from time import clock
import frontmatter
from slugify import slugify


POST_FOLDER = 'content/post'


def search_in_title(title, search):
    return slugify(search.lower()) in slugify(title.lower())


def sort_post_wrapper(orderby):
    def sort_post(item):
        return item.get(orderby)
    return sort_post

# Simpler orderby just because it's not produciton code
def lister(search=None, orderby='-date', offset=0, count=10):
    found = []
    for filename in os.listdir(POST_FOLDER):
        path = '%s/%s' % (POST_FOLDER, filename)
        post = frontmatter.load(path)

        if post.get('title') and (not search or search_in_title(post.get('title', ''), search)):
            found.append({
                'path': path,
                'title': post.get('title'),
                'date': datetime.strptime(post.get('date'), "%Y-%m-%d %H:%M:%S-00:00"),
                'categrories': post.get('categories', [])
            })

    reverse = orderby[0] == '-'
    orderby = orderby[1:] if reverse else orderby
    ordered = sorted(found, key=sort_post_wrapper(orderby), reverse=reverse)

    return {
        'items': ordered[offset:offset + count],
        'more': len(ordered[offset:offset + count + 1]) > count
    }


def run():
    start = clock()
    res = lister()
    elapsed = clock() - start
    print "Simple list: %ss for %s items" % (elapsed, len(res.get('items')))

    start = clock()
    res = lister(search='My Post')
    elapsed = clock() - start
    print "Filtered list: %ss for %s items" % (elapsed, len(res.get('items')))

    start = clock()
    res = lister(orderby='date')
    elapsed = clock() - start
    print "Ordered list: %ss for %s items" % (elapsed, len(res.get('items')))

    start = clock()
    res = lister(orderby='date', offset=50, count=50)
    elapsed = clock() - start
    print "Big list: %ss for %s items" % (elapsed, len(res.get('items')))


if __name__ == "__main__":
    run()
