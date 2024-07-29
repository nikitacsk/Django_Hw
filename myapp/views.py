from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import random
import string
from .forms import UserForm, AuthenticationForm, ApplicantForm, RegistrationForm, ChangePasswordForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
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


def form_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # some actions
            return render(request, 'myapp/form_was_valid.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'myapp/form.html', {'form': form})


def my_login(request):
    form = AuthenticationForm(request.POST or None)
    if form.is_valid():
        login(request, form.user)
        return HttpResponseRedirect('/')
    return render(request,  'myapp/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')  # Redirect to a success page.


@login_required(login_url='/login')
def change_pass(request):
    return HttpResponseRedirect('/')


def check_applicant(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            if form.is_valid_applicant():
                message = "You are suitable according to the data"
            else:
                message = "You are not suitable according to the data"
            return render(request, 'myapp/result.html', {'message': message})
    else:
        form = ApplicantForm()

    return render(request, 'myapp/applicant_form.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('private_page')
    else:
        form = RegistrationForm()
    return render(request, 'myapp/register.html', {'form': form})


@login_required
def private_page(request):
    return render(request, 'myapp/private_page.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password1']
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            return redirect('password_change_done')
    else:
        form = ChangePasswordForm(user=request.user)
    return render(request, 'myapp/change_password.html', {'form': form})
