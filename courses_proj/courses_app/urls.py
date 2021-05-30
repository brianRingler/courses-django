from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('courses/', views.add_courses_view, name='add_courses'),
    path('courses/delete/<int:id_del>/', views.delete_courses_view, name='delete_courses'),
    path('courses/comment/<int:id_rate>/', views.comment_courses_view, name='comment_courses'),

]