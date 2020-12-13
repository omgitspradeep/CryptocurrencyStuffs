from django.urls import path,include
from .views import (
    home,
    detail,
    )

urlpatterns = [
    path('', home, name="home"),
    path('detail/', detail, name="detail"),

]