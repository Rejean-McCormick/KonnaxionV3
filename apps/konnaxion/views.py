from django.http import HttpResponse

def debug_test(request):
    return HttpResponse("Debug test is working!")
