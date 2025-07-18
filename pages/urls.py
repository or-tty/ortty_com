from django.urls import path

from .views import home_view, games_view

app_name = 'pages'

urlpatterns = [
    path('', home_view, name='home'),
    path('games/', games_view, name='games'),
]