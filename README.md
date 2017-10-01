# Test node file listing performance

I wanted to make sure that I could manage all my blog posts directly on a filesystem instead of having to cache them in a database. To be sure it is viable, I made this small project that build around 5000 fake posts (at 1 post a week, it's almost a hundred year of blogging), and test the performance of listing and searching through those files. You can learn more on [my blog](http://maleandre.fr/2017/10/01/node-web-app-without-database/).

## How to run it

If you're using Docker, you should have Docker installed, that's all. If you run everything directly in your local environment, you need Node, yarn, pip, virtualenv. Everything will be cleaned up at the end of the test.

On your local machine:

```bash
./run.sh
```

In a docker container:

```bash
./docker.sh
```
