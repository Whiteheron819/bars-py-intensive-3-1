from django.urls import path

from . import views

urlpatterns = [
    path('create_workers/', views.create_workers, name='create'),
    path('main_base/', views.main, name='main'),
    path('replica_base/', views.replica, name='replica'),
    path('choose_db', views.choose_db, name='choice')
]
