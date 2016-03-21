from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sumar(request, num1, num2):
    suma = int(num1) + int(num2)
    return HttpResponse("<b><h1>" + "Sumamos: " + str(num1) + " + " +
                        str(num2) + " = " + str(suma)+ "</h1></b>")

def restar(request, num1, num2):
    resta = int(num1) - int(num2)
    return HttpResponse("<b><h1>" + "Restamos: " + str(num1) + " - " +
                        str(num2) + " = " + str(resta)+ "</h1></b>")

def multiplicar(request, num1, num2):
    mult = int(num1) * int(num2)
    return HttpResponse("<b><h1>" + "Multiplicamos: " + str(num1) + " * " +
                        str(num2) + " = " + str(mult)+ "</h1></b>")

def dividir(request, num1, num2):
    div = int(num1) / int(num2)
    return HttpResponse("<b><h1>" + "Dividimos: " + str(num1) + " / " +
                        str(num2) + " = " + str(div)+ "</h1></b>")

def error(request):
    return HttpResponse('<b><h1><font color="red">404 Not Found</font></h1></b>')
