import json

from django.views.generic import TemplateView
from rest_framework.renderers import JSONRenderer
from django.core import serializers

from .models import JourneyStep, Project, SkillCategory, Skill, Connect
from .serializers import SkillCategorySerializer, SkillSerializer


class HomePage(TemplateView):
    template_name = 'resume/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['JourneySteps'] = JourneyStep.objects.all()
        context['Projects'] = Project.objects.all()
        context['SkillCategories'] = SkillCategory.objects.all()
        context['Connects'] = Connect.objects.all()

        skills = dict()
        for cat in context['SkillCategories']:
            skills[cat.name] = Skill.objects.filter(category=cat)
        context['Skills'] = skills

        categories = SkillCategory.objects.all()
        serializer = SkillCategorySerializer(categories, many=True)
        context['Skillsjsonserializer'] = serializer.data

        return context
