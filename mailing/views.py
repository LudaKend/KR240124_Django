from django.shortcuts import render

def index_home_page(requests):
    context = {
        'name_page': 'Главная'
    }
    return render(requests, 'mailing/home_page.html', context)
