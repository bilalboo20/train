from django.shortcuts import render

def home_page(request):
    return render(request, 'index.html')
def AIdetales(request):
    return render(request, 'AIdetales.html')
def AIbad(request):
    return render(request, 'AIbad.html')
def contact(request):
    return render(request, 'contact.html')
def about_us(request):
    return render(request, 'about_us.html')