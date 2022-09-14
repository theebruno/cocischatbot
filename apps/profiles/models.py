"""
foo comment
"""
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify  # very important for using site/username.xxx
from django.urls import reverse

from apps.lecturer_offices.models import LecturerOffice

User = get_user_model()


# class ProfileManager(models.Manager):
#     """
#     foo comment
#     """


class Profile(models.Model):
    """
    """
    user = models.OneToOneField(User, primary_key=True, related_name='profile',
                                on_delete=models.CASCADE)  # user.profile
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField("Short Bio", max_length=500, blank=True, null=True)
    profile_pic = models.ImageField('Profile picture', upload_to='profile_pics/%Y-%m-%d/',
                                    null=True, blank=True, default="img/faces/avatar.jpg")
    phone_number = models.CharField(blank=True, null=True, max_length=255)
    office = models.ForeignKey(LecturerOffice, max_length=255, blank=True, null=True,
                               on_delete=models.DO_NOTHING)
    email = models.EmailField(null=False, blank=False)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)

    # objects = ProfileManager()

    def __str__(self):
        # return self.user.username
        return '{} {}'.format(self.first_name, self.last_name)

    # fn() below is handling the saving of our profile's slug field
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    @property
    def image_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url

    # this method must be defined for appropriate url mapping in comments section
    def get_absolute_url(self):
        return reverse('profiles:show_self_details', kwargs={'slug': self.slug})


def post_save_user_receiver(instance, created, **kwargs):
    """
    """

    if created:
        Profile.objects.get_or_create(user=instance)


post_save.connect(post_save_user_receiver, sender=User)
