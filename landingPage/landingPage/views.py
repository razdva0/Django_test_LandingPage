from django.http import HttpResponse
from django.shortcuts import render


def first_page(request):
    hello = 'Hello'
    text = 'New text'
    return render(request, './index.html', {
        'hello': hello,
        'text': text
    })
