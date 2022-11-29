from django.urls import path
from . import views
urlpatterns = [
    path('',views.showData),
    path('add_data.html',views.addData),
    
]