from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Course


class CourseList(ListView):
    model = Course
    template_name = "courses/list.html"
    context_object_name = "courses"

    def get_queryset(self):
        query = self.request.GET.get("q")
        sort = self.request.GET.get("sort")

        if query:
            que = Course.objects.filter(
                Q(title__icontains=query) | Q(teacher__icontains=query)
            )
        else:
            que = Course.objects.all()


        if sort == "created_at":
            que = que.order_by("-created_at")

        return que
    
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