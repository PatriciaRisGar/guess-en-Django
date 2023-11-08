from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'guess/home.html')

def guess_request(request):
    number = random.randint(1, 100)
    userData = int(request.POST['guess'])

    if userData == number:
        msg = ' Enhorabuena'
    elif userData > number:
        msg = ' Demasiado alto'
    else:
        msg = 'Muy bajo'

    return render(request, 'guess/resultado.html', {'msg': msg})