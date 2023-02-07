from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Card
from .forms import CardForm
# Create your views here.

def create_view(request):
    context = {}
    form = CardForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    
    context['form'] = form
    return render(request, 'cards/create_view.html', context)

def list_view(request):
    context = {}
    context['cardset'] = Card.objects.all()
    return render(request, 'cards/list_view.html', context)

def detail_view(request, id):
    context = {}
    card = Card.objects.get(id=id)
    context['card'] = card
    return render(request, 'cards/detail_view.html', context)

def update_view(request, id):
    context = {}
    obj = get_object_or_404(Card, id=id)
    form = CardForm(request.POST, request.FILES, instance=obj)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    
    context['form'] = form
    return render(request, 'cards/update_view.html', context)

def delete_view(request, id):
    obj = get_object_or_404(Card, id=id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect('/')
    
    return render(request, 'cards/delete_view.html', {'card': obj})