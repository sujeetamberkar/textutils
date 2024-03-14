# I have created this file - SUJEET AMBERKAR
import string
from django.http import HttpResponse
from django.shortcuts import render
def index (request):
    # return HttpResponse("HOME")
    params = {'name':'Sujeet'}
    return render(request,"index.html",params) #Request and name of the server 

def ex1(request):
    pass
def analze(request):
    text = request.POST.get('text', '').strip()
    if not text:  # Check if text is empty after stripping whitespace
        text = 'SAMPLE'  # Default value if no text is entered
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps','off')
    # print(text)
    # print(removepunc)

    if removepunc == "on":
        var = ""
        for charater in text:
            if charater  not in string.punctuation:
                var = var + charater
        text = var

    if fullcaps == "on":
        text=text.upper()
    params = {'analyzedtext':text}
    
    return render(request,"analze.html",params)