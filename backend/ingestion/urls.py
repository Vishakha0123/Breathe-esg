from django.urls import path
from . import views

urlpatterns = [
    path("upload/",views.upload_file),
    path("activities/",views.activities),
    path("activities/<int:pk>/approve/", views.approve_activity),
path("activities/<int:pk>/lock/", views.lock_activity),
]