from django.urls import path,include
from .views import (
    home,
    prices
    )

urlpatterns = [
    path('', home, name="home"),
    path('prices/', prices, name="prices"),

]