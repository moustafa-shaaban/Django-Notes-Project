from django.db import models
from django.conf import settings


class Note(models.Model):
    """Model definition for Note."""

    title = models.CharField(max_length=250)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        """Meta definition for Note."""

        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

    def __str__(self):
        """Unicode representation of Note."""
        return f'Note Title: {self.title}, By: {self.user}'