from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from tasks.forms import TaskCreateView
from tasks.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all()


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateView
    success_url = reverse_lazy("tasks:index")
    template_name = "tasks/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")
    template_name = "tasks/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")
    template_name = "tasks/task_confirm_delete.html"


def done_task(request, pk):
    task = Task.objects.get(id=pk)
    if task.done is True:
        task.done = False
        task.save()
    else:
        task.done = True
        task.save()
    return HttpResponseRedirect(reverse("tasks:index"))


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "tasks/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "tasks/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "tasks/tag_confirm_delete.html"
