from django.urls import path
from .views import TaskView, CategoryView, TagView

urlpatterns = [
    path("tasks", TaskView.as_view(), name="tasks"),
    path("tasks/<int:task_id>", TaskView.as_view(), name="tasks"),
    path("categories", CategoryView.as_view(), name="categories"),
    path("categories/<int:category_id>", CategoryView.as_view(), name="categories"),
    path("tags", TagView.as_view(), name="tags"),
    path("tags/<int:tag_id>", TagView.as_view(), name="tags"),
]
