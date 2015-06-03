# from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Poll


class PollList(ListView):
    model = Poll
    template_name = "poll_list.html"
    context_object_name = "polls"


class PollDetails(DetailView):
    model = Poll
    template_name = "poll_details.html"
    context_object_name = "poll"
    pk_url_kwarg = "poll_id"

# def poll_list(request):
#     # construct a queryset
#     qs = get_list_or_404(Poll)
#     return render(request, "poll_list.html", {"polls": qs})

# def poll_details(request, poll_id):
#     poll = get_object_or_404(Poll, pk=poll_id)
#
#     return render(request, "poll_details.html", {"poll": poll})