"""
URL mappings for the user API.
"""
from django.urls import path

from user import views


app_name = 'user' #reverse mapping

urlpatterns = [
    path('create/', views.CreateUserView.as_view()#class based view django supported 
    , name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]