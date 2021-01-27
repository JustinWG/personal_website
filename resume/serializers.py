from rest_framework import serializers

from .models import Skill, SkillCategory


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'stars']
        # fields = '__all__'


class SkillCategorySerializer(serializers.ModelSerializer):
    # skills = SkillSerializer(source='skill_set', many=True)
    skills = SkillSerializer(many=True)

    class Meta:
        model = SkillCategory
        fields = ['name', 'skills']
