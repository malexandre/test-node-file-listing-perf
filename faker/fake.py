# Create specified number of articles for HDD benchmarks
# inspired by Hugo Benchmark from @Jaden https://gist.github.com/jaden/1ce5a7192d8ee8e4c112

import os
import shutil
from datetime import datetime
import random
import string


def generate_word():
    length = random.randint(1, 10)
    word = ''.join(random.choice(string.letters) for _ in range(length))
    return word


def generate_sentence(words):
    return ' '.join([generate_word() for _ in range(words)])


def get_random_date():
    year = random.choice(range(1950, 2015))
    month = random.choice(range(1, 13))
    day = random.choice(range(1, 29))
    hours = random.choice(range(0, 24))
    minutes = random.choice(range(0, 60))
    seconds = random.choice(range(0, 60))
    return datetime(year, month, day, hours, minutes, seconds)


def create_post(output_dir, categories, title=None):
    desc = generate_sentence(100)
    cat = random.choice(categories)
    date = get_random_date()

    if not title:
        title = generate_sentence(8)

    slug = title.replace(' ', '-').lower()
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')

    with open('%s/%s.md' % (output_dir, date.strftime("%Y-%m-%d_%H-%M-%S")), 'w') as file_post:
        file_post.write('---\n')
        file_post.write('title: "%s"\n' % title)
        file_post.write('description: "%s"\n' % desc)
        file_post.write('categories: ["%s"]\n' % cat)
        # Use UTC time to avoid having to mess with timezones and daylight saving time
        file_post.write('date: "%s"\n' % date.strftime("%Y-%m-%d %H:%M:%S-00:00"))
        file_post.write('slug: "%s"\n' % slug)
        file_post.write('---\n\n')
        # Generate blocks of random words
        num_paragraphs = random.randint(5, 10)
        for _ in range(num_paragraphs):
            file_post.write(generate_sentence(random.randint(150, 300)))
            file_post.write('\n\n')

def run():
    # Set defaults
    output_dir = 'content/post'
    num_posts = 5000
    num_categories = 10

    # Generate random categories
    categories = [generate_word() for _ in range(num_categories)]

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    os.makedirs(output_dir)

    print "Staring fake posts build..."
    for i in range(num_posts):
        create_post(output_dir, categories)
        if i % 100 == 0:
            print "Built %s posts" % i

    create_post(output_dir, categories, "My Post 1")
    create_post(output_dir, categories, "My Post 2")
    create_post(output_dir, categories, "My Post 3")
    create_post(output_dir, categories, "My Post 4")
    create_post(output_dir, categories, "My Post 5")
    print "All fake posts created"


if __name__ == "__main__":
    run()
