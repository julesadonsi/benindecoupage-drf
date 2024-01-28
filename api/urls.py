from django.urls import path

from .views import (
    DepartmentTownView,
    DepartmentView,
    NeighborhoodsView,
    TownDistrictsView
)

urlpatterns = [
    path("departments/", DepartmentView.as_view()),
    path("departments/<pk>/towns", DepartmentTownView.as_view()),
    path("towns/<pk>/districts", TownDistrictsView.as_view()),
    path("districts/<pk>/neighborhoods", NeighborhoodsView.as_view()),
]
