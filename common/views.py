from django.shortcuts import render

from common import models
from common.models import *


def index(request):
    model = TestModel.objects.all()

    last_title = model.last().title
    last_count = model.last().count

    data = {
        "test1": 312121212,
        "count": last_count,
        "title": last_title,
    }
    return render(request, 'common/index.html', context=data)


from django.shortcuts import render
from .models import Card, Outdoor, WhyUsCard, ProcessCard, StatisticCard, Monitor


def card(request):
    cards = Card.objects.all()
    outdoors = Outdoor.objects.all()
    why_us_cards = WhyUsCard.objects.filter(is_active=True).order_by('order')
    processcard = ProcessCard.objects.all().order_by('number')
    statisticcard = StatisticCard.objects.all().order_by('order')
    monitor = Monitor.objects.all().order_by('title')

    first_card = cards.first()
    last_card = cards.last()
    first_outdoor = outdoors.first()
    last_outdoor = outdoors.last()

    first_count = first_card.count if first_card else 0
    last_count = last_card.count if last_card else 0
    last_word = last_outdoor.word if last_outdoor else ""

    first_title = first_outdoor.title if first_outdoor else ""
    last_title = last_outdoor.title if last_outdoor else ""

    first_icon = first_outdoor.icon if first_outdoor else ""
    last_icon = last_outdoor.icon if last_outdoor else ""

    card_data = {
        "first_count": first_count,
        "last_count": last_count,
        "last_title": last_title,
        "first_title": first_title,
        "word": {
            "now": last_word
        },
        "title": {
            "new": first_title,
            "now": last_title
        },
        "icon": last_icon,
        "steps": first_icon,
        "why_us_cards": why_us_cards,
        "processcard": processcard,
        "statisticcard": statisticcard,
        "monitor": monitor
    }


    context = {
        'card': card_data,  # Bu tepadagi 'card.cards', 'card.partners' kabi eski kodlarni ishlatadi
        'monitor': monitor,  # Bu pastdagi '{% for item in monitor %}' tsiklini ishlatadi
        'why_us_cards': why_us_cards,
        'processcard': processcard,
        'statisticcard': statisticcard,
    }

    print(context)  # Tekshirish uchun terminalga chiqarish
    return render(request, 'common/index.html', context=context)


# def outdoor(request):
#     outdoors = Outdoor.objects.all()
#
#     last_word = outdoors.last().word
#     last_title= outdoors.last().title
#
#     outdoor= {
#         "word":last_word,
#         "title":last_title,
#     }
#     print(outdoors)
#     return render(request, 'common/index.html', context=outdoor)