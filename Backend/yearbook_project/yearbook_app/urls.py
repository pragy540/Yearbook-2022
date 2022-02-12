from . import views
from django.urls import path

urlpatterns = [
    # path('', views.index, name='index'),
    # path('profile/', views.profile_disp),
    # path('addprof/', views.add_person),
    path('register/', views.register, name="index"),
    path('profile/', views.profile)
]
