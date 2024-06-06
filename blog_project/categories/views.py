from django.shortcuts import render
from django.http import HttpResponse
from .forms import CategoryForm

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})