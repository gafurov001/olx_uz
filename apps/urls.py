from django.urls import path, include

urlpatterns = [
    path("", include("ads.urls")),
    path("", include("users.urls"))
]