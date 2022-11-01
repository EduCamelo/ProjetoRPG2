from django.shortcuts import render
from RPG.forms import Personagem

def registro(request):
    return render(request, 'registro.html')

def personagem(request):
        form=Personagem()
        contexto={'form': form}
        return render(request, 'personagem.html', contexto)

def revConsulta(request):
    if request.method =='POST':
        form = Personagem(request.POST)
        contexto={'form': form}
        return render(request, 'consulta.html',contexto)

def luta1(request):
    return render(request, 'luta1.html')

def luta2(request):
    return render(request, 'luta2.html')

def luta3(request):
    return render(request, 'luta3.html')

def lutaFinal(request):
    return render(request, 'lutaFinal.html')

def derrota(request):
    return render(request, 'derrota.html')
