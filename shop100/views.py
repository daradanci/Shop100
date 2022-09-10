from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
#from database import cloth_types, models
from shop100.models import Range, Models, Stock

def hello(request):
    return render(request, 'index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})

def Start(request):
    # return render(request, 'start.html', {'data' : {
    #     'current_date': date.today(),
    #     'types': cloth_types
    # }})
    return render(request, 'start.html', {'data':
        Range.objects.all()
    })

def GetClothes(request, id):
    # return render(request, 'Clothes.html', {'data' : {
    #     'current_date': date.today(),
    #     'id': id,
    #     'models': models[id-1]['stock']
    # }})

    return render(request, 'Clothes.html', { 'data':{
        'id': id,
        'range': Range.objects.filter(rangeid=id)[0],
        'models': GetModels(id),
        # 'stock': GetStock(id)
    }})

def GetSizes(request, id, modelid):
    return render(request, 'Stock.html', { 'data':{
        'id':id,
        'modelid':modelid,
        'model':Models.objects.filter(modelid=modelid)[0],
        'stock':GetStock(modelid),
    }})
def GetModels(id):
    return Models.objects.filter(idrange=id)


def GetStock(id):
    return Stock.objects.filter(idmodel=id)

def rangeList(request):
    print(Range.objects.all())
    return render(request, 'test.html', {'data':
        Range.objects.all()
    })

cloth_types = [
            {'title': 'Верхняя одежда', 'id': 1},
            {'title': 'Костюмы', 'id': 2},
            {'title': 'Обувь', 'id': 3},
        ]

models = [
    {'type': 1, 'stock':
     [
         {'name': 'Чёрная шуба', 'price': '20000Р', 'producer': 'Турция', 'img':'images/coat2.png'},
         {'name': 'Белая шуба', 'price': '18000Р', 'producer': 'Турция', 'img': 'images/coat2.webp'},
         {'name': 'Куртка <<Зима>>', 'price': '10000Р', 'producer': 'Москва', 'img': 'images/kurtka.jpg'},
     ]},

    {'type': 2, 'stock':
    [
        {'name': 'Чёрный нуар', 'price': '7000Р', 'producer': 'Франция', 'img':'images/uni2.jpg'},
        {'name': 'Белая кобра', 'price': '8000Р', 'producer': 'Москва', 'img':'images/uni1.jpg'},
    ]},
    {'type': 2, 'stock':
    [
        {'name': 'Ласточки', 'price': '5000Р', 'producer': 'Москва', 'img':'images/sneakers2.jpg'},
        {'name': 'Модники', 'price': '6000Р', 'producer': 'Москва', 'img':'images/sneakers1.jpg'},
    ]},

]

