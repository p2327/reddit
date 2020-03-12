import os 
import jinja2


def render(filename: jinja2.Template, context: dict) -> str:
    """
    Generate html from a jinja2 template.
    Args:
        filename: jinja2 template
        context: dict of variables to pass in
    Returns:
        rendered HTML from jinja 2 template engine
    """
    # Using __file__ combined with various os.path 
    # modules lets all paths be relative the current 
    # module's directory location
    path = os.path.dirname(os.path.abspath(__file__))
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)