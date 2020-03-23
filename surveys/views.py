from django.shortcuts import HttpResponse, redirect

def Surveys(request):
    return HttpResponse('placeholder to display all the surveys created')

def surveysNew(request):
    return HttpResponse('placeholder for users to add a new survey')
    