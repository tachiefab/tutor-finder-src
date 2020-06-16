from django.db import models
from .signals import parsed_hashtags

class Subject(models.Model):
	name = models.CharField(max_length=500)
	count = models.BigIntegerField(default=0)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


	def __str__(self):
		return self.name


def parsed_hashtags_receiver(sender, hashtag_list, *args, **kwargs):
    if len(hashtag_list) > 0:
        for tag_var in hashtag_list:
            new_tag, create = Subject.objects.get_or_create(name=tag_var)
parsed_hashtags.connect(parsed_hashtags_receiver)