from django.http import HttpResponse


def question(request):
    return HttpResponse("Question")

def main(request):
    return HttpResponse("Main.");

def addquestion(request):
    return HttpResponse("Addquestion");

def login(request):
    return HttpResponse("Login");

def registration(request):
    return HttpResponse("Registration");

