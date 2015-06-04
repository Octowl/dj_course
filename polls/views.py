from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView

from .models import Poll, Choice
from .forms import ResponseForm, PollForm, InlineChoiceFormset


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


def poll_response(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)

    # check if the user is posting data
    if request.method == 'POST':
        # create a bounded form
        form = ResponseForm(request.POST)
        # validate the data
        if form.is_valid():
            # # we no have validated data in cleaned_data
            # # get the respondent choice object
            # r_choice = form.cleaned_data['choice']
            # # get the respondent comment
            # r_comment = form.cleaned_data['comment']
            #
            # # create the new response entry using our choice reverse selection
            # r_choice.response_set.create(
            #     comment=r_comment,
            # )
            form.save()

            messages.success(request, 'Your response was successfully posted')

            # now redirect to poll list
            return redirect('poll_list')

    # if not POST, then the user opened this view for the first time
    else:
        # present an unbounded form
        form = ResponseForm()
        # filter options for choice displaying only ones for current poll
        form.fields['choice'].queryset = Choice.objects.filter(poll=poll)

    return render(
        request,
        'poll_response.html',
        {
            'poll': poll,
            'form': form,
        }
    )

def poll_create(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        formset = None
        if form.is_valid():
            poll = form.save(commit=False)
            formset = InlineChoiceFormset(request.POST, instance=poll)
            if formset.is_valid():
                poll.save()
                formset.save()
                messages.success(request,'Poll was successfully created.')
                return redirect('poll_list')
    else:
        form = PollForm()
        formset = InlineChoiceFormset(instance=Poll())

    if not formset:
        formset = InlineChoiceFormset(instance=poll)

    return render(
        request,
        'poll_create.html',
        {
            "form": form,
            "formset": formset,
        }
    )


def poll_edit(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    # enable ability to delete choices
    InlineChoiceFormset.can_delete = True
    formset = None

    if request.method == 'POST':
        form = PollForm(request.POST, instance=poll)
        if form.is_valid():
            formset = InlineChoiceFormset(request.POST, instance=poll)
            if formset.is_valid():
                form.save()  # this will update object
                formset.save()  # this will update objects
                messages.success(request, 'Poll was successfully edited.')
                return redirect('poll_list')
    else:
        # both form and formset are bound to
        # the poll object we are editing
        form = PollForm(instance=poll)

    if not formset:
        formset = InlineChoiceFormset(instance=poll)

    return render(
        request,
        'poll_edit.html',
        {
            "poll": poll,
            "form": form,
            "formset": formset,
        }
    )