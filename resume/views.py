from django.views.generic import TemplateView
from .models import JourneyStep, Project


class HomePage(TemplateView):
    template_name = 'resume/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['JourneySteps'] = JourneyStep.objects.all()
        context['Projects'] = Project.objects.all()
        return context
