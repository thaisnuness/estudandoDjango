from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transacao
from .form import TransacaoForm
import datetime

def home(request):
    data = {}
    data['clientes'] = ['c1', 'c2', 'c3']
    data['now'] = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render (request,'contas/listagem.html', data)

def nova_transacao(request):
    form = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    return render (request, 'contas/form.html', {'form':form})

def update(request, pk):
    form = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    return render (request, 'contas/form.html', {'form':form})
