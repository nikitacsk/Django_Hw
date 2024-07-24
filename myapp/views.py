from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world")

def my_url(request):
    return HttpResponse("Hello it's my_url")

def acricles(request):
    return HttpResponse("Hello it's acricles")

def acrticles_archive(request):
    return HttpResponse("Hello it's acrticles_archive")

def users(request):
    return HttpResponse("Hello it's users")

def article(request, article_number):
    return HttpResponse(f"Hello it's article ")

def article_slug(request, article_number, slug_text=''):
    return HttpResponse(f"Hello it's article number {article_number}, text is {slug_text}")

def users_id(request, user_number):
    return HttpResponse(f"Hello it's users {user_number}")

def phone_function(request, phone_number):
    return HttpResponse(f"Ваш номер телефону: {phone_number}")

def custom_view(request, year):
    return HttpResponse(f"Ваш параметр: {year}")
