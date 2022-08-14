from django.views.generic import TemplateView

class ProfileView(TemplateView):
    template_name = "pages/profile.html"