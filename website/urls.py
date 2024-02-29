from django.urls import path
from django.views.generic import RedirectView
from django.views.defaults import page_not_found

from .views.project_view import ProjectListView, ProjectIndexView, ProjectLogCreateView
from .views.space_views import SpaceListView, SpaceIndexView


urlpatterns = [
    path('spaces/<int:space_id>/projects', ProjectListView.as_view(), name="website-project-list"),
    path('spaces/<int:space_id>/projects/<int:project_id>/', ProjectIndexView.as_view(), name="website-project-index"),
    path('spaces/<int:space_id>/projects/<int:project_id>/create-log', ProjectLogCreateView.as_view(), name="website-project-create-log"),
]
