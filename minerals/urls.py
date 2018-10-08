from django.urls import path


from . import views


app_name = 'minerals'
urlpatterns = [
    path('', views.mineral_list, name='index'),
    path('<int:pk>/', views.mineral_detail, name='detail'),
    path('random_mineral', views.random_mineral, name='random_mineral'),
]

