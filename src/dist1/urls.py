from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('task/<int:id>', views.taskView, name="task-view"),
    path('newtask/', views.NewTask, name="new-task"),
    path('edittask/<int:id>', views.EditTask, name="edit-task"),
    path('deltask/<int:id>', views.DelTask, name="del-task"),
    path('checktask/<int:id>', views.checktask, name="check-task"),
]
