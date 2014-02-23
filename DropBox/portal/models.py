from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
def get_upload_path(instance, filename):
	return os.path.join('files', instance.owner.username, filename)

class UploadFile(models.Model):
	#file = models.FileField(upload_to='files/%Y/%m/%d')
	file = models.FileField(upload_to=get_upload_path)