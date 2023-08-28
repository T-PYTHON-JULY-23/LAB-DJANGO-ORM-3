from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("add/", views.add_post_view, name="add_post_view"),
    path("all/", views.all_post_view, name="all_post_view"),
    path("", views.home_view, name="home_view"),
    path("detail/<post_id>/", views.post_detail_view, name="post_detail_view"),
    path("update/<post_id>/", views.post_update_view, name="post_update_view"),
    path("delete/<post_id>/", views.post_delete_view, name="post_delete_view"),
    path("search/", views.search_view, name="search_view"),


]
