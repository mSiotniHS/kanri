js_template := '''
(function () {
    if (document.querySelector(<#INSERT#>)) {
        <#CODE#>
    }
})()
'''

py_template := '''
from django_components import component

@component.register("${component_name}")
class ${component_name_uppercamel}(component.Component):
    template_name = '${component_name}/${component_name}.html'

    def get_context_data(self):
        # set params here
        pass
    
    class Media:
        css = '${component_name}/${component_name}.css'
        js = '${component_name}/${component_name}.js'
'''

ls:
    just --list

manage +COMMAND:
    python manage.py {{ COMMAND }}

create-comp-folder-and-files COMPONENT_NAME:
    mkdir components/{{ COMPONENT_NAME }}
    touch components/{{ COMPONENT_NAME }}/{{ COMPONENT_NAME }}.css
    touch components/{{ COMPONENT_NAME }}/{{ COMPONENT_NAME }}.html
    touch components/{{ COMPONENT_NAME }}/{{ COMPONENT_NAME }}.js
    touch components/{{ COMPONENT_NAME }}/{{ COMPONENT_NAME }}.py

comp COMPONENT_NAME: (create-comp-folder-and-files COMPONENT_NAME)
    #!/usr/bin/env python

    from string import Template

    js_template = """{{js_template}}"""
    py_template = """{{py_template}}"""

    with open("components/{{ COMPONENT_NAME }}/{{ COMPONENT_NAME }}.js", "w") as js_file:
        js_file.write(js_template)
    
    with open("components/{{ COMPONENT_NAME }}/{{ COMPONENT_NAME }}.py", "w") as py_file:
        py_file.write(Template(py_template).substitute(
            component_name="{{ COMPONENT_NAME }}",
            component_name_uppercamel="{{ uppercamelcase(COMPONENT_NAME) }}"
        ))

run:
    just manage runserver & just manage tailwind start

cs: (manage "collectstatic")
