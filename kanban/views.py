from django.shortcuts import render
from .models import Card, List


def view_kanban_board(request):
    lists = List.objects.prefetch_related("cards")
    return render(request, "kanban/kanban.html", {"lists": lists})
