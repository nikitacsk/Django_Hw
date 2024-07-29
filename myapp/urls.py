from django.urls import path, re_path
from django.views.generic import TemplateView

from . import views
from myapp.views import index, articles, articles_archive, users, article, article_slug, users_id, form_view, my_login, \
    logout_view, change_pass

phone_regex = r'^0(39|50|63|66|67|68|91|92|93|94|95|96|97|98|99)\d{7}$'

urlpatterns = [
    path('', index, name='idx'),
    path('login', my_login, name='login-url'),
    path('logout', logout_view, name='logout-url'),
    path('change-password', change_pass, name='change'),
    path('form/', views.check_applicant, name='check_applicant'),
    path('register/', views.register, name='register'),
    path('private/', views.private_page, name='private_page'),
    path('change-password/', views.change_password, name='change_password'),
    path('password-change-done/', TemplateView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('form-url/', form_view, name='form-view'),
    path('articles/', articles),
    path('articles/archive/', articles_archive),
    path('users/', users),
    path('article/<int:article_number>', article, name='number'),
    path('article/<int:article_number>/archive', article_slug),
    path('article/<int:article_number>/<slug:slug_text>', article_slug, name='slug'),
    path('users/<int:user_number>', users_id),
    re_path(r'^phone/(?P<phone_number>0(39|50|63|66|67|68|91|92|93|94|95|96|97|98|99)[0-9]{7})/$', views.phone_function, name='phone_number'),
    re_path(r'custom/(?P<year>[1-9a-f]{4}-[1-9a-f]{6})/$', views.custom_view),
]
