from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse("Hello, world. You're at the index.")

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html')
