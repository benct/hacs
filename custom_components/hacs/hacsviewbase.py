"""Blueprint for HacsViewBase."""
from homeassistant.components.http import HomeAssistantView
from jinja2 import Environment, PackageLoader

from .hacsbase import HacsBase

class HacsViewBase(HomeAssistantView, HacsBase):
    """Base View Class for HACS."""

    requires_auth = False

    def render(self, templatefile, location=None, repository=None):
        """Render a template file."""
        loader = Environment(loader=PackageLoader('custom_components.hacs.frontend'))
        template = loader.get_template(templatefile + '.html')
        return template.render({"hacs": self, "location": location, "repository": repository})

    def load_element(self, element):
        """return element content."""
        location = "{}/custom_components/hacs/frontend/elements/{}.html".format(self.config_dir, element)
        with open(location, "r") as elementfile:
            content = elementfile.read()
            elementfile.close()
        return content

    @property
    def base_content(self):
        """Base content."""
        return self.render('base')

    @property
    def footer(self):
        """Return the end of the document."""
        return "</div></body>"
