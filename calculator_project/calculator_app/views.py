from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    if request.method=='POST':
        result=None
        number1=float(request.POST.get('number1'))
        number2=float(request.POST.get('number2'))
        operator=request.POST.get('Operation')
        if operator=="Add":
            result=number1+number2
        elif operator=="Sub":
            result=number1-number2
        elif operator=="Mul":
            result=number1*number2
        else:
            if number2!=0:
                result=0
            else:
                result=number1/number1
    else:
        result="Please Enter Details"
    return render(request,'cal.html',{'result':result})

def clear(request):
    result="Please Enter Details"
    return render(request,'cal.html',{'result':result})