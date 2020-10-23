from django.shortcuts import render

# Create your views here.
def bye(request):
    return render(request, 'settingapp/bye.html')

def option(request):
    return render(request, 'settingapp/option.html')



