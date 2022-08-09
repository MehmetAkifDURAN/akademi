from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('courses/<slug:slug_category>', views.getCoursesByCategory,
         name='get_courses_by_category')
]
