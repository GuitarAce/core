from django.urls import path
from apps import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('login/', views.loginPage, name='login'),
    # path('register/', views.registerPage, name="register"),
    path('project-list/', views.projectList, name='project-list'),
    path('project-create/', views.projectCreate, name='project-create'),
    path('project-edit/<int:id>', views.projectEdit, name='project-edit'),
    path('project-delete/<int:id>', views.projectDelete, name='project-delete')
]
