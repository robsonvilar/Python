# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from . forms import TecladoTelefoneForm


def teclado_telefone(request):
    if request.method == 'POST':
        form = TecladoTelefoneForm(request.POST)
        if form.is_valid():
            numero = form.cleaned_data['numero_telefone']

            # Chame a função que faz a requisição para a API aqui
            resposta_api = fazer_requisicao_api(numero)

            return HttpResponse(resposta_api)
    else:
        form = TecladoTelefoneForm()

    return render(request, 'teclado_telefone.html', {'form': form})


def fazer_requisicao_api(numero):
    try:
        api_url = f"https://viacep.com.br/ws/{numero}/json/"

        requisicao = requests.get(api_url, timeout=3)
        resultado = requisicao.json()

        lista_resultado = []
        lista_resultado.append(resultado)

        # return f"CEP: {resultado['cep']}, BAIRRO: {resultado['bairro']}, LOCALIDADE: {resultado['localidade']}"
        return lista_resultado
    except Exception as erro:
        return f"Erro identificado: {erro}"
