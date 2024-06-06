from django.shortcuts import render
from django.http import HttpResponse
from .forms import AuthorForm

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})
