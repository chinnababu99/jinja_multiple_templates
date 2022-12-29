from django.shortcuts import render

# Create your views here.
def user(request):
    d={'name':'chinna babu','age':21,'mno':8074691119}
    return render (request,'user.html',context=d)
def user1(request):
    details={'name':'ravi','age':23,'mno':'9347811171'}
    return render(request,'user1.html',details)