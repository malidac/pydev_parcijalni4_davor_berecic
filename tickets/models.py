from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Ticket(models.Model):
    class Status(models.TextChoices):
        NEW = "new", _("New")
        OPEN = "open", _("Open")
        IN_PROGRESS = "in_progress", _("In progress")
        DONE = "done", _("Done")
        CLOSED = "closed", _("Closed")


    title = models.CharField(max_length=150,
                             null=False,
                             blank=False)
    description = models.TextField(null=False,
                                   blank=False)
    status = models.CharField(max_length=15,
                              choices=Status,
                              default=Status.NEW,)

    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.DO_NOTHING,
                                    related_name='reported_tickets',
                                    null=False,
                                    blank=False)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.DO_NOTHING,
                                    related_name='assigned_tickets',
                                    null=True,
                                    blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} - ({self.status})'