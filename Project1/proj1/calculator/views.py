from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def calc(request):
    return render(request,'calculator.html')

def submit(request):
    q = request.GET['query']
    try:
        ans=eval(q) # takes a string as input and evaluate as mathematical equation
        mydict ={
            "q":q,
            "ans":ans,
            "error":False,
            "result":True
        }
        return render(request,"calculator.html",context=mydict)
    except:
        mydict={
            "error":True,
            "result":False
        }
        return render(request,"calculator.html",context=mydict)
