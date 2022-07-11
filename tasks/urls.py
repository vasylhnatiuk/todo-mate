from django.contrib.auth import views
from django.urls import path

from .views import TaskListView, TagListView, TagCreateView, \
    TagUpdateView, TagDeleteView, TaskCreateView, TaskUpdateView, \
    TaskDeleteView, done_task

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path(
        "create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "index/<int:pk>/done/",
        done_task,
        name="done-task"
    ),
    path("tags/",
         TagListView.as_view(),
         name="tag-list"),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),

]
app_name = "task"

