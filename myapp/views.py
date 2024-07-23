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


def acricles(request):
    data = {'text': 'acricles'}
    return render(request, 'myapp/static.html', data)


def acrticles_archive(request):
    data = {'text': 'acrticles_archive'}
    return render(request, 'myapp/static.html', data)


def users(request):
    data = {'text': 'users'}
    return render(request, 'myapp/static.html', data)


def article(request, article_number):
    data = {
        'article_number': article_number,
        'bool': article_number % 2
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
    return HttpResponse(f"Ваш номер телефону: {phone_number}")


def custom_view(request, year):
    return HttpResponse(f"Ваш параметр: {year}")
