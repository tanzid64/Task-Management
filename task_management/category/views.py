from django.shortcuts import render, redirect
from . import forms, models
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        category_form = forms.AddCategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')

    category_form = forms.AddCategoryForm()
    return render(request, 'add_category.html', {'form': category_form})