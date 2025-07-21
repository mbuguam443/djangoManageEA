from django.urls import path
from . import views

urlpatterns = [
    path("", views.ea_settings_list, name="ea_settings_list"),
    path("create/", views.ea_settings_create, name="ea_settings_create"),
    path("edit/<int:id>/", views.ea_settings_edit, name="ea_settings_edit"),
    path("delete/<int:id>/", views.ea_settings_delete, name="ea_settings_delete"),


]
