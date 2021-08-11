from django.shortcuts import render
from passagens.forms import PassagemForms


def index(request):
    template_name = 'index.html'
    form = PassagemForms()
    context = {
        'form': form
        }
    return render(request, template_name, context)
