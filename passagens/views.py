from django.shortcuts import render
from passagens.forms import PassagemForms


def index(request):
    template_name = 'index.html'
    form = PassagemForms()
    context = {
        'form': form
        }
    return render(request, template_name, context)


def revisao_consulta(request):
    template_name = 'consulta.html'
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        context = {
            'form': form
            }
    return render(request, template_name, context)
