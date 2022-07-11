from django import forms
from django.forms import DateTimeInput

from tasks.models import Task


class TaskCreateView(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"




