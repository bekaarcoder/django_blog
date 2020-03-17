from django.shortcuts import render

posts = [
  {
    'author': 'Shashank',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'March 17, 2019'
  },
  {
    'author': 'John',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'March 17, 2019'
  }
]

def index(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/index.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})
