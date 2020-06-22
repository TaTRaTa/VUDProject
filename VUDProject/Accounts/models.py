from django.db import models
from django.contrib.auth.models import User

# There is two type of users: 1 for donor and 0 for needy. 
# For this purpose the new flag attribute donorOrNeedy has been added to User model. By default is needy.
class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    donorOrNeedy = models.PositiveSmallIntegerField(default=0)
