from typing import Mapping, Any

from django.urls import reverse

from ..models import Project, Space, Inbox


class BaseStructureMixin:
    """
    Mixin that adds context_data, necessary for rendering
    "base_structure" based templates.
    """

    @property
    def space_id(self) -> int:
        return self.kwargs['space_id']

    def get_context_data(self, **kwargs: Mapping[str, Any]) -> Mapping[str, Any]:
        context = super().get_context_data(**kwargs)

        context['current_space'] = {
            'id': self.space_id,
            'name': Space.objects.get(id=self.space_id)
        }

        context['base_links'] = [
            {
                'route': 'website-space-index',
                'label': 'Overview',
                'count': None,
            },
            {
                'route': 'website-space-inbox',
                'label': 'Inbox',
                'count': Inbox.objects.filter(space__id=self.space_id, someday=False).count(),
            },
            {
                'route': 'website-project-list',
                'label': 'Projects',
                'count': Project.objects.filter(space__id=self.space_id, archived=False).count(),
            },
            {
                'route': 'website-space-someday',
                'label': 'Someday',
                'count': Inbox.objects.filter(space__id=self.space_id, someday=True).count(),
            },
            {
                'route': 'website-space-archive',
                'label': 'Archive',
                'count': None,
            }
        ]

        for base_link in context['base_links']:
            base_link['route'] = reverse(base_link['route'], args=[self.space_id])
            base_link['current'] = base_link['route'] == self.request.path

        context['nav_projects'] = Project.objects.all()[:5]

        return context
