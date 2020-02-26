from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户名')
	nickname = models.CharField(max_length=20, verbose_name='昵称')

	def __str__(self):
		return '<Profile: %s for %s>' % (self.nickname, self.user.username)

#获取昵称
def get_nickname(self):
	if Profile.objects.filter(user=self).exists():
		profile = Profile.objects.get(user=self)
		return profile.nickname
	else:
		return ''
#获取昵称或用户名
def has_nickname_or_username(self):
	if Profile.objects.filter(user=self).exists():
		profile = Profile.objects.get(user=self)
		return profile.nickname
	else:
		return self.username
#拥有昵称
def has_nickname(self):
	return Profile.objects.filter(user=self).exists()

#动态绑定
User.get_nickname = get_nickname
User.has_nickname = has_nickname
User.has_nickname_or_username = has_nickname_or_username