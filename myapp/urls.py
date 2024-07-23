
from django.urls import path, re_path
from . import views
from myapp.views import index, acricles, acrticles_archive, users, article, article_slug, users_id


phone_regex = r'^0(39|50|63|66|67|68|91|92|93|94|95|96|97|98|99)\d{7}$'

urlpatterns = [
    path('', index, name='idx'),
    path('acricles/', acricles),
    path('acrticles/archive/', acrticles_archive),
    path('users/', users),
    path('articles/<int:article_number>', article),
    path('article/<int:article_number>/archive', article_slug),
    path('article/<int:article_number>/<slug:slug_text>', article_slug),
    path('users/<int:user_number>', users_id),
    re_path(r'^phone/(?P<phone_number>0(39|50|63|66|67|68|91|92|93|94|95|96|97|98|99)[0-9]{7})/$', views.phone_function, name='phone_number'),
    re_path(r'custom/(?P<year>[1-9a-f]{4}-[1-9a-f]{6})/$', views.custom_view),
]
