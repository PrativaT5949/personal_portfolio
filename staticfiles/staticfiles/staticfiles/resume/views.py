from django.views.generic import TemplateView
from resume.models import Experience, Education, Professionalskill, language


class ResumeView(TemplateView):
    template_name = 'resume.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experiences'] = Experience.objects.all()
        context['education_list'] = Education.objects.all()
        context['skills'] = Professionalskill.objects.all()
        context['languages'] = language.objects.all()
        return context
