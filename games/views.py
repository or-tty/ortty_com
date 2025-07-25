from django.shortcuts import get_object_or_404, render
from .models import Game


def game_list(request):
    games = Game.objects.all()
    return render(
        request,
        'games/list.html',
        {'games': games}
    )


def game_detail(request, slug):
    game = get_object_or_404(
        Game,
        slug=slug,
    )
    return render(
        request,
        'games/detail.html',
        {'game': game}
    )