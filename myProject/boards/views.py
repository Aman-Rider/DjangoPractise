from django.shortcuts import render,get_object_or_404,redirect
from .models import Board,User,Topic,Post
from .forms import NewTopicForm

# Create your views here
def home(request):
    board = Board.objects.all()
    
    return render(request,'home.html',{'boards':board})

def board_topics(request,pk):
    board = get_object_or_404(Board,pk=pk)
    return render(request,'topics.html',{'board':board})


def new_topic(request,pk):
    board = get_object_or_404(Board, pk=pk)
    form = NewTopicForm()
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
              
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )

            return redirect('board_topics', pk=board.pk)  
    return render(request, 'new_topic.html',  {'board': board, 'form': form})