from typing import Mapping, Any

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from . import BaseStructureMixin
from ..models import Project, Task, ProjectLog


class ProjectViewsMixin:
    @property
    def project_id(self) -> int:
        return self.kwargs['project_id']


class ProjectListView(BaseStructureMixin, TemplateView):
    template_name = 'website/project/list.html'

    def get_context_data(self, **kwargs: Mapping[str, Any]) -> Mapping[str, Any]:
        context = super().get_context_data(**kwargs)

        context['projects'] = Project.objects.filter(space__id=self.space_id, archived=False)

        return context


class ProjectIndexView(BaseStructureMixin, ProjectViewsMixin, TemplateView):
    template_name = 'website/project/index.html'

    def get_context_data(self, **kwargs: Mapping[str, Any]) -> Mapping[str, Any]:
        context = super().get_context_data(**kwargs)

        project = Project.objects.get(id=self.project_id, space__id=self.space_id)
        tasks = Task.objects.filter(project__id=self.project_id)
        logs = ProjectLog.objects.filter(project__id=self.project_id).order_by('-timestamp')

        context['project'] = project
        context['tasks'] = tasks
        context['logs'] = logs

        return context


class ProjectLogCreateView(View):
    template_name = 'website/project/created_log.html'

    def post(self, request, **kwargs):
        log_text = request.POST.get('log-text', None)

        if not log_text:
            return render(request, self.template_name, {'log': None})

        space_id: int = kwargs['space_id']
        project_id: int = kwargs['project_id']

        project = Project.objects.get(id=project_id, space__id=space_id)

        log = ProjectLog(
            project=project,
            text=log_text
        )
        log.save()

        return render(request, self.template_name, {'log': log})
