from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    print(request.user)
    print(request.GET)
    print(request.session)
    return HttpResponse(f"Hello <h1>{request.user}</h1>")
