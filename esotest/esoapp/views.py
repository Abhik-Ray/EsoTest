from django.shortcuts import render
import brainfuck as bf
# Create your views here.


def index(request):
    return render(request, 'esoapp/index.html')


def brainfuck(request):
    command = "code here"
    result = 'hello'
    if request.GET:
        print("Here!")
        command = request.GET['command']
        result = bf.evaluate(command)
    return render(request, 'esoapp/brainfuck.html', {"command": command, "result": result})


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


def esochoose(request):
    return render(request, 'esoapp/esochoose.html')
