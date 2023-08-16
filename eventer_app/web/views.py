from django.http import HttpRequest
from django.shortcuts import render, redirect

from eventer_app.web.forms import CreateProfileForm, CreateEventForm, EditEventForm, DeleteEventForm, EditProfileForm, \
    DeleteProfileForm
from eventer_app.web.models import Profile, Event


def get_profile():
    return Profile.objects.first()


def get_all_events():
    return Event.objects.all() if Event.objects.all() else None


def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'shared/home-page.html', context)


def dashboard(request):
    profile = get_profile()
    events = get_all_events()
    context = {
        'profile': profile,
        'events': events,
    }
    return render(request, 'events/dashboard.html', context)


def create_event(request):
    profile = get_profile()
    form = CreateEventForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'events/event-create.html', context)


def details_event(request, pk):
    event = Event.objects.get(pk=pk)
    profile = get_profile()

    context = {
        'event': event,
        'profile': profile,

    }
    return render(request, 'events/events-details.html', context)


def edit_event(request, pk):
    event = Event.objects.get(pk=pk)
    profile = get_profile()

    form = EditEventForm(instance=event)
    if request.method == 'POST':
        form = EditEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'event': event,
        'form': form,
        'profile': profile,
    }
    return render(request, 'events/event-edit.html', context)


def delete_event(request, pk):
    profile = get_profile()
    event = Event.objects.get(pk=pk)

    form = DeleteEventForm(instance=event)
    if request.method == 'POST':
        event.delete()
        return redirect('dashboard')

    context = {
        'event': event,
        'form': form,
        'profile': profile,
    }
    return render(request, 'events/events-delete.html', context)


def create_profile(request):
    profile = get_profile()
    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,

    }
    return render(request, 'profiles/profile-create.html', context)


def details_profile(request):
    profile = get_profile()
    total_events = Event.objects.count()

    context = {
        'profile': profile,
        'total_events': total_events,

    }
    return render(request, 'profiles/profile-details.html', context)


def edit_profile(request):
    profile = get_profile()

    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('details-profile')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profiles/profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'profiles/profile-delete.html', context)
