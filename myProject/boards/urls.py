from django.urls import path
from django.conf.urls import url
from boards import views
urlpatterns = [
    path('',views.home,name='home'),
    path('<int:pk>',views.board_topics, name='board_topics'),
    path('<int:pk>/new',views.new_topic,name='new_topic'),
]
