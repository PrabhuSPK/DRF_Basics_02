from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('index2',views.index2,name='index2'),
    path('throttle',views.throttle,name='throttle'),
    path('schema',views.schema,name='schema'),

    path('users/', views.ListUsers.as_view()),

    

  
]