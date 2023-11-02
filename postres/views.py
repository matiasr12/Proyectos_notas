from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def profesor(request):
    return render(request,'profesor.html')


def notas(request):
    return render(request, 'notas.html')


def anotaciones (request):
    return render(request,'anotaciones.html')

def actividadesp(request):
    return render(request,'actividadesp.html')


def alumno(request):
    return render(request,'alumno.html')


def notasal(request):
    return render(request,'notasal.html')

def actividadesal(request):
    return render(request,'actividadesal.html')

def logina(request):
    return render(request,'loginalumno.html')

def loginp(request):
    return render(request,'login_profesor.html')

def loginap(request):
    return render(request,"loginapoderado.html")

def apoderados(request):
    return render(request,"apoderados.html")
