from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Entity
from .serializers import EntitySerializer
from .forms import EntityForm


class HomeView(TemplateView):
    template_name = "pages/home.html"


class EntityListView(LoginRequiredMixin, FormView):
    template_name = "pages/app.html"
    model = Entity
    serializer = EntitySerializer
    form_class = EntityForm
    
    def get_success_url(self) -> str:
        return reverse("app")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = self.model.objects.filter(
            created_by = self.request.user)

        return context

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        cleaned_data["created_by"] = self.request.user.id
        serializer = self.serializer(data=cleaned_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return super().form_valid(form)