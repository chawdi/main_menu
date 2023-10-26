from django.db import models
from django.contrib.sites.models import Site
from django.urls import reverse

class MenuItem(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    named_url = models.CharField(max_length=100, blank=True, null=True)
    menu_name = models.CharField(max_length=100, default="default_menu")

    def has_children(self):
        return self.children.exists()

    def get_absolute_url(self):
        return reverse('menu:menu_item_view', args=[str(self.named_url)])

    def get_ancestors(self):
        ancestors = []
        current = self.parent
        while current:
            ancestors.append(current)
            current = current.parent
        return ancestors

    def __str__(self):
        return self.title
