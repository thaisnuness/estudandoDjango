from django.shortcuts import render
from django.http import HttpResponse
from .models import Transacao
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