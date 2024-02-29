from website.models import ProjectLog

from django_components import component


@component.register("log_entry")
class LogEntry(component.Component):
    template_name = 'log_entry/log_entry.html'

    def get_context_data(self, log: ProjectLog):
        return {
            'log': log
        }
