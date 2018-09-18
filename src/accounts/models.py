from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save

CPNUMBER_REGEX = '(09)\d{9}$'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    cellphone_number = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                regex=CPNUMBER_REGEX,
                message='Cellphone Number format [0917xxxxxxx].',
                code='Invalid Cellphone Number'
            )
        ])

    def __str__(self):
        return str(self.user.username)


def post_save_user_model_receiver(sender, instance, created,  *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except ():
            pass


post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
