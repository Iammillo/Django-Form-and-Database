from django.urls import path
from . import views

urlpatterns=[
            path("submit/",views.submit),
            path("",views.index),
            path("search/",views.search),

]
