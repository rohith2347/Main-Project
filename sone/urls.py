from django.urls import path
from . import views
#from django.conf import settings
#from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('start-game/', views.game, name='start_game'),
    path('result/', views.result, name='result'),
]
