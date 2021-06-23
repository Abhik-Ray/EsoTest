from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'esoapp/index.html')


def brainfuck(request):
    return render(request, 'esoapp/brainfuck.html')


def about(request):
    return render(request, 'esoapp/about.html')


def spl(request):
    return render(request, 'esoapp/spl.html')


def malbolge(request):
    return render(request, 'esoapp/malbolge.html')


def esoterrible(request):
    return render(request, 'esoapp/esoterrible.html')


def example(request):
    return render(request, 'esoapp/example.html')
