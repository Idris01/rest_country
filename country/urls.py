from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/country/", views.CountryListView.as_view()),
    path("api/<str:continent>/country/", views.ContinentAPIView.as_view()),
]
