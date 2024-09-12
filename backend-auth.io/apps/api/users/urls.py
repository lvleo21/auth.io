from django.urls import path, include

urlpatterns = [
    path("v1/", include("apps.api.users.v1.urls"))
]
