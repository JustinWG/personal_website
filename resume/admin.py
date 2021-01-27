from django.contrib import admin
from .models import JourneyStep, Project, SkillCategory, Skill, Connect


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'stars')


admin.site.register(JourneyStep)
admin.site.register(Project)
admin.site.register(SkillCategory)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Connect)
