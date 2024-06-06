from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProfileForm

def add_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm()
    return render(request, 'add_profile.html', {'form': form})
