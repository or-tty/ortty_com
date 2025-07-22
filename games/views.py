from django.shortcuts import render

def games_view(request):
    return render(
        request, 'games/games.html'
    )