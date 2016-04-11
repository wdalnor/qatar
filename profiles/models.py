from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




class Userprofile(models.Model):


	user = models.OneToOneField(User)
	bio = models.TextField(default='bio default')
	picture = models.ImageField(upload_to = "profile_images/%Y/%m/%d", blank = True)

	def __str__(self):
		return self.user.username


@receiver(post_save,sender=User)
def create_profiel(sender, **kwargs):
	if kwargs.get('created', False):
	    Userprofile.objects.get_or_create(user=kwargs.get('instance'))