from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page


class ExplorerPage(Page):
    """Collection Explorer landing page."""

    introduction = models.CharField(max_length=200, blank=False)

    content_panels = Page.content_panels + [FieldPanel("introduction")]

    parent_page_types = ["home.HomePage"]