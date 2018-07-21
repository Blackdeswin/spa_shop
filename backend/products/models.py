from django.db import models
from django.utils.translation import ugettext_lazy as _


class Products(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    price = models.IntegerField(default=1)
    image = models.CharField(max_length=24, blank=True, null=True, default=None)
    category = models.CharField(max_length=24, blank=True, null=True, default=None)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)


    def __str__(self):
        return self.name

    # @property
    # def announce(self):
    #     return self.announce_text or self.text[:512].rsplit(' ', 1)[0]

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('products')
        verbose_name_plural = _('products')
