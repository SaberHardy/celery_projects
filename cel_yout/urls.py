from django.urls import path

from cel_yout import views

urlpatterns = [
    path('list', views.FibonacciListView.as_view(), name='list'),
    path('start', views.FibonacciView.as_view(), name='start'),
]
