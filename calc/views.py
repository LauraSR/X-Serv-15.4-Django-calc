from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def suma(request, op1, op2):
    suma = int(op1) + int(op2)
return HttpResponse("Resultado: " op1 + " + " + op2 + " = " + str(suma))

def resta(request, op1, op2):
    resta = int(op1) - int(op2)
    return HttpResponse("Resultado: " op1 + " - " + op2 + " = " + str(resta))


def multi(request, op1, op2):
    multi = int(op) * int(op)
    return HttpResponse("Resultado: " op + " * " + op2 + " = " + str(multi))

def divi(request, op1, op2):
    try:
        divi = int(op1) / int(op2)
    except ZeroDivisionError:
        return HttpResponse("No puedes dividir entre 0")

    return HttpResponse("Resultado: " op1 + " / " + op2 + " = " + str(divi))

def error(request):
    return HttpResponse('Not Found')
