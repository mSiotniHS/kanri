from django_components import component

@component.register("nav_drawer_link")
class NavDrawerLink(component.Component):
    template_name = 'nav_drawer_link/nav_drawer_link.html'

    def get_context_data(self, current: bool = False):
        return {
            'current': current
        }
