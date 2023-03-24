# maths/urls.py
from django.urls import path
from .views import math, add, sub, mul, div, maths_list, math_details, results_list, maths_list_by_operation

app_name="maths"
urlpatterns = [
   path('', math),
   path('add/<int:a>/<b>', add),
   path('sub/<int:a>/<b>', sub),
   path('mul/<int:a>/<b>', mul),
   path('div/<int:a>/<b>', div),
   path('histories/', maths_list, name="list"),
   path('histories/<int:id>', math_details, name="details"),
   path('results/', results_list, name="results"),
   path('histories/list_by_operation/', maths_list_by_operation, name="list_by_operation"),
]