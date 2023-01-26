
from django.urls import path
from .views import *

urlpatterns=[
    path('items/',ItemsListView.as_view()),
    path('items/<int:pk>/',ItemsDetailView.as_view())

    ]