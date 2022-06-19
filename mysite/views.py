from django.http import HttpResponse
from django.shortcuts import render
from sympy import dirichlet_eta

def index(request):
    return render(request,'index.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text','default')

    # check checkbox value
    removepunc = request.POST.get('removepunc','off')
    capson = request.POST.get('capson','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    
    # check which checkbox is on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        # analyze the text
        para ={'purpose':'Removed punctuations','Analyzed_text':analyzed}
        djtext = analyzed

    if capson == 'on':
        analyzed = ""
        analyzed+=djtext.upper()
        para ={'purpose':'capitalized','Analyzed_text':analyzed}
        jtext = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '/n' and char!="\r":
                analyzed+=char
        # analyze the text
        para ={'purpose':'Removed new line','Analyzed_text':analyzed}
        jtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index,char in enumerate(djtext):
            if index+1<len(djtext) and (not (djtext[index] == " " and djtext[index + 1] == " ")):
                analyzed+=char
        # analyze the text
        para ={'purpose':'Removed extra space','Analyzed_text':analyzed}
    
    if(removepunc!="on" and capson!="on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse("Error!!! select any option and try again")


    return render(request,'analyze.html',para)
