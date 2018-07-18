from django.shortcuts import render


# Create your views here.
def register(request):
    return render(request, "register.html")


def login_in(request):
    dic = {}
    if request.POST:
        dic['username'] = request.POST['username']

        return render(request,"login.html",dic)
    return render(request, "login.html")
