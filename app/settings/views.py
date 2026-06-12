from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy

from .models import Course


class CourseList(ListView):
    model = Course
    template_name = "courses/list.html"
    context_object_name = "courses"

    def get_queryset(self):
        query = self.request.GET.get("q")

        if query:
            return Course.objects.filter(
                title__icontains=query
            )
        
        return Course.objects.all()

class CourseCreate(CreateView):
    model = Course
    template_name = "courses/create.html"
    fields = "__all__"
    success_url = reverse_lazy("list")

class CourseUpdate(UpdateView):
    model = Course
    template_name = "courses/update.html"
    fields = "__all__"
    success_url = reverse_lazy("list")

class CourseDelete(DeleteView):
    model = Course
    template_name = "courses/delete.html"
    success_url = reverse_lazy("list")