from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Add this line to map the index view
    path('admin/', admin.site.urls),
]

