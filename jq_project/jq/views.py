from django.shortcuts import render
from django.http import JsonResponse
from .models import Feedback

# Create your views here.
def index(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'home.html', {'feedbacks': feedbacks})

def add_feedback(request):
    if request.method == 'POST':
        feedback=Feedback.objects.create(
        name=request.POST.get('name'),
        comments=request.POST.get('comments'),
        )
    
    return JsonResponse({
        'id':feedback.id,
        'name':feedback.name,
        'comments':feedback.comments
    })
