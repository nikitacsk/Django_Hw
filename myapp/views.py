from django.http import HttpResponse
from django.shortcuts import render
import random
import string
# Create your views here.


def index(request):

    num = random.randint(1, 100)
    length = random.randint(5, 10)
    slug = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    data = {
        'num': num,
        'slug': slug,
    }

    return render(
        request,
        'myapp/index.html',
        data
    )


def my_url(request):
    data = {'text': 'my_url'}
    return render(request, 'myapp/static.html', data)


def articles(request):
    data = {'text': 'articles'}
    return render(request, 'myapp/static.html', data)


def articles_archive(request):
    data = {'text': 'articles_archive'}
    return render(request, 'myapp/static.html', data)


def users(request):
    data = {'text': 'users'}
    return render(request, 'myapp/static.html', data)


def article(request, article_number):
    data = {
        'article_number': article_number,
        'is_odd': article_number % 2
            }
    return render(
        request,
        'myapp/article_number.html',
        data
    )


def article_slug(request, article_number, slug_text=''):
    data = {'article_number': article_number, 'slug_text': slug_text}
    return render(
        request,
        'myapp/article_slug.html',
        data
    )


def users_id(request, user_number):
    return HttpResponse(f"Hello it's users {user_number}")


def phone_function(request, phone_number):
    return HttpResponse(f"Your phone number: {phone_number}")


def custom_view(request, year):
    return HttpResponse(f"Your year: {year}")
