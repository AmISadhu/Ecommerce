from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver


@receiver(pre_save, sender=User)
def hask_passwd(sender, instance, **kwargs):
    if (instance.id is None) or (sender.objects.get(id=instance.id).password != instance.password):
        instance.set_password(instance.password)
