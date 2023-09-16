from django.urls import path
from game import views

app_name = 'game'

urlpatterns = [
    path('', views.index, name='index'),
    path('make_move/<int:position>/', views.make_move, name='make_move'),
]
