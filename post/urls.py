from django.urls import path

from . import views

app_name = 'post'
urlpatterns = [
    path('novo_topico/', views.newTopic, name="newTopic"),
]
