
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns=[
    path('items/',ItemList.as_view()),
    path('items/<int:pk>/',ItemDetail.as_view()),
    # path('items/<int:pk>/',ItemsDetailView.as_view())

    ]

urlpatterns = format_suffix_patterns(urlpatterns)