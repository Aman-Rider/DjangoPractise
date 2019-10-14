from django.shortcuts import render
from .models import Board
# Create your views here
def home(request):
    board = Board.objects.all()
    
    return render(request,'home.html',{'boards':board})
