from django.shortcuts import render
import brainfuck as bf
from esoapp.malbolge import *
from esoapp.definitions import definitions

# Create your views here.


def index(request):
    return render(request, "esoapp/index.html")


def brainfuck(request):
    command = "code here"
    result = "hello"
    if request.GET:
        print("Here!")
        command = request.GET["command"]
        result = bf.evaluate(command)
    return render(
        request, "esoapp/brainfuck.html", {"command": command, "result": result}
    )


def about(request):
    return render(request, "esoapp/about.html")


def spl(request):
    return render(request, "esoapp/spl.html")


def esoterrible(request):
    return render(request, "esoapp/esoterrible.html")


def malbolge(request):
    d = definitions()
    command = d.get_examples("malbolge")
    result = "hello"
    if request.GET:
        command = request.GET["command"]
        result = feedInstructions(command)
    return render(
        request,
        "esoapp/esoterrible.html",
        {"command": command, "result": result, "lang": "Malbolge"},
    )


def example(request):
    return render(request, "esoapp/example.html")


def esochoose(request):
    return render(request, "esoapp/esochoose.html")
