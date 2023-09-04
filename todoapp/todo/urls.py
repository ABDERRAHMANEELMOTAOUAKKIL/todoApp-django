from django.urls import path
from .views import HomePageView, TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('tasks/', TaskList.as_view(),name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(),name='task_detail'),
    path('task/create/', TaskCreate.as_view(),name='task_create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(),name='task_update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(),name='task_delete'),





]