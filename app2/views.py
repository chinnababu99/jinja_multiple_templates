from django.shortcuts import render

# Create your views here.
def user2(request):
    s={'name':'madhura','age':22}
    return render(request,'user2.html',context=s)

def user3(request):
    m={'name':'meghasree','age':21}
    return render (request,'user3.html',m)
