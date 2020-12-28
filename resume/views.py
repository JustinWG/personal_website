from django.views.generic import TemplateView
from .models import JourneyStep, Project, SkillCategory, Skill


class HomePage(TemplateView):
    template_name = 'resume/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['JourneySteps'] = JourneyStep.objects.all()
        context['Projects'] = Project.objects.all()
        context['SkillCategories'] = SkillCategory.objects.all()
        context['Skill'] = Skill.objects.all()
        return context
