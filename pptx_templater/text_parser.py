from jinja2 import Template


def render(text, **kwargs):
    template = Template(text)
    return template.render(**kwargs)
