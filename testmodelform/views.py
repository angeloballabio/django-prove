
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .forms import PostCartellaForm
from .models import Cartella

# Create your views here.


def index(request):

    context = {}

    # carica la pagina principale che si trova in pmodelform/templates
    return render(request, 'index.html', context=context)


def testform(request):
    elenco_cartelle = Cartella.objects.all()
    if request.method == 'POST':
        form = PostCartellaForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/testform/')

    form = PostCartellaForm
    context = {'form': form, 'cartelle': elenco_cartelle}
    return render(request, 'testform.html', context=context)


def ModificaPubblicita(request, pk):
    elenco_cartelle = Cartella.objects.all()
    cartella = get_object_or_404(Cartella, pk=pk)
    if request.method == "POST":
        form = PostCartellaForm(request.POST, instance=cartella)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/testform/')
         

    form = PostCartellaForm(instance=cartella)
    context = {'form': form, 'cartelle': elenco_cartelle}
    return render(request, 'modifytestform.html', context=context)
