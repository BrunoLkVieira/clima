from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests

# Create your views here.


def Homepage(request):
    template = loader.get_template('homepage.html')

    termo_pesquisa = request.GET.get("query")

    if termo_pesquisa:
        city_name = termo_pesquisa


        API_key = "4a71427592c2f8eb4461cfa3e380dd0f"

        link= f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&lang=pt_br&appid={API_key}"

        requisicao = requests.get(link).json()

        descricao_clima = requisicao["weather"][0]["description"]
        temperatura= round((requisicao["main"]["temp"] - 273.15))
        umidade = f"{requisicao['main']['humidity']}%"
        vento = f"{round(requisicao['wind']['speed'] * 3.6)} km/h"




        context = {
            'descricao_clima': descricao_clima,
            'temperatura': temperatura,
            'umidade': umidade,
            'vento': vento,
            'cidade':  city_name
        }
        return HttpResponse(template.render(context, request))

    else:
        return render(request, "homepage.html")

