
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    #params={'name':'Tridipa','place':'Pune'}
    return render(request,'index.html')

'''def removepunc(request):
    mytext = request.GET.get('text','default')
    return HttpResponse('Removed Punctuation from given text')
'''
def analyze(request):
    mytext = request.GET.get('text', 'off')
    mycheckbox = request.GET.get('mycheckbox','default')
    upbox = request.GET.get('upbox', 'off')
    capbox = request.GET.get('capbox', 'off')
    charbox = request.GET.get('charbox', 'off')
    punctuations= '''(){}'\/&@#$%*!^[]-_<>'''
    analyzed = ""
    if mycheckbox == "on":
        for char in mytext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': "after removing Punctuation is ", 'analyzed_text': analyzed}
        return render(request,'analyze.html', params)
    elif upbox =="on":
        for char in mytext:
            analyzed=analyzed+char.upper()
        params={'purpose': "Converted to upper case ",'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

    elif capbox =="on":
        for char in mytext:
            analyzed = analyzed+char.lower()
        params={'purpose':"Capitalized text is ",'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

    elif charbox =="on":
        for char in mytext:
            analyzed=analyzed+char
            totalcont=len(analyzed)
        params={'purpose':"total number of characters",'analyzed_text':totalcont}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error no checkbox selected")
'''def uprcase(request):
    return HttpResponse('Text converted to UPPERCASE')



def lwrcase(request):
    return HttpResponse('Text converted to lowercase')

def charcount(request):
    return HttpResponse('Counted total number of character in given input')
'''