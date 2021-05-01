# I have created this file -tayyab

from django.http import HttpResponse
from django.shortcuts import render

# this is a first function of the dganjo series
# def index(request):
#     return HttpResponse("hello django i am here") 

# tut_5
# this function is just use to path of the url
# def about(request):
#     return HttpResponse("about dejango this is my first code in dganjo") 
# tut_6
# this function is as a exercise which we use link to go to the 5 webbsites
# def links(request):
#     return HttpResponse("<h2>Welcom</h2>this is my youtube channal <a target='blank' href='https://www.youtube.com/watch?v=H_h9m7J8rUs&list=PLAVoEuLcnUS4FVqFTOlBp9I9zKR3ZrNS7&index=9'>click here</a><br>  This is my facebook page <a target='blank' href='https://web.facebook.com/?_rdc=1&_rdr'>click here</a><br> this is my instagram account<a target='blank' href='https://www.instagram.com/'>click here</a><br> this is the vedio pixals website<a target='blank' href = 'https://www.pexels.com/'>click here</a><br> this the you tube link <a target = 'blank' href='https://www.youtube.com/'>click here</a>" )
# tut_7 ----laying the pipeline---
# these functions are the pipline of textUtil website
# def index(request):
#     return HttpResponse("Home")
# def removepun(request):
#     djtext = request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse("this is the remove punchuation <a href='/'>back</a>")
# def capitilizefirst(request):
#     return HttpResponse("this is the capitilize first of the word <a href='/'>back</a>")
# def newlineremove(request):
#     return HttpResponse("this page helps to remove the new line <a href='/'>back</a>")
# def spaceremove(request):
#     return HttpResponse("this page helps to remove the space between the woreds <a href='/'>back</a>")
# def charcount(request):
#     return HttpResponse("this page helps to charactors out <a href='/'>back</a>")

# tut_8 ----django templates 
# we use django templates first off all add in the 'setting.py' in templates arry in DIRS with the name of templates
# then create a for with the name of templates and in this folder we create html files and write any thing whic we want to do
# then we import the templates as 'from django.shortcuts import render' and then we use rendor function
# achully rendor function given three arguments first 'request' 2nd 'html file name' and 3rd if we creat dictionary 
# dictionary is creat is the view page but it retrive and use in the html file

# def indexrender(request):
#     dic={"name":"tayyab","place":"pakistan"}
#     return render(request, 'indexrender.html',dic)

# tut_9 ---creating homepage of our textUtil website
def index(request):
    return render(request, 'index.html')

# tut_10 -----coding the backend
# in this tutorial we create backend as a textUtils website
def analyze(request):
    # ////////////////Get the text
    djtext=request.POST.get('text','default')
    # //////////////////////checkbox check the value is it exit or not
    removepun = request.POST.get('removepunc','off')
    uppercase= request.POST.get('uppercase','off')
    newlineremove= request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    # analyzed=djtext
    # return HttpResponse("this is the analyze of the website")
    # these are the signs of punchations 
    punchation = '''!()-[]{'};:'"\,<>./?@#$%^&*_+~'''
    # /////////////////check which chickbox is on or not////
    # ---------------# return render(request,'analyze.html',params) this code is commented kue k hum na sab ka leya ek he necha ba dia tha ta ka sab ka sab hum ek he dafa ma dakh saka-----------
    if removepun== "on":
        analyzed = ""
        for char in djtext:
            if char not in punchation:
                analyzed = analyzed + char
        params={"purpose":"Remove Punchuation" , "analyzed_text":analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if uppercase=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={"purpose":"All charactors is UPPER CASE","analyzed_text":analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if newlineremove=="on":
        analyzed=""
        for char in djtext:
            if (char != "\n" and char!="\r"):
                analyzed = analyzed+char
        params ={"purpose":"Remove the new Line charactor","analyzed_text":analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html',params)
    if (extraspaceremover=="on"):
        analyzed =""
        for index , char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed+char
        params = {"purpose":"remove the space","analyzed_text":analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if (charcount =="on"):
        analyzed = djtext.count("")
        params = {"purpose":"remove the space","analyzed_text":analyzed}
        djtext = analyzed
    if (removepun != "on" and uppercase !="on" and newlineremove !="on" and extraspaceremover !="on" and charcount !="on"):
        return HttpResponse("ERROR! Please select the operations and try again")
        # return render(request,'analyze.html',params)
    return render(request,'analyze.html',params)
    # else:
    #     return HttpResponse("Error ")