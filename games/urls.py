from django.urls import path

from .views import games_view

app_name = 'games'

urlpatterns = [
    path('', games_view, name='games'),
]