from django.urls import path
from .views import Mutual_Fund_List
urlpatterns = [
path('',Mutual_Fund_List.as_view(), name='employee'),
]