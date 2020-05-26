from django.urls import path
from .import views
from form.views import Exam_View,addform
urlpatterns=[
    path('',views.post_list,name='post_list'),
    path('form/',Exam_View),
    path('add/',addform),
]