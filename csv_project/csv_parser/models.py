from django.db import models
from django.contrib.auth.models import User

# https://docs.djangoproject.com/en/1.11/ref/contrib/auth/
# his fields:
# username, first_name, last_name, email, password, groups
# user_permissions, is_staff, is_active, is_superuser,
# last_login, date_joined


class CSVFile(models.Model):
    path = models.CharField(max_length=128, default="File_path")
    file = models.FileField(upload_to='files/', default="Server_path")
    creation_date = models.DateTimeField(auto_now=True)
    my_user = models.ForeignKey(User)

    @property
    def file_info(self):
        return "Added: {} by {}".format(self.creation_date
                                            .strftime("%Y-%m-%d, %H:%M:%S"),
                                        self.my_user.username)

    def __str__(self):
        return "ID:" + str(self.id) + " " + self.file_info


class CSVModel(models.Model):
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now=True)
    field_1 = models.CharField(max_length=100)
    field_2 = models.CharField(max_length=100)
    field_3 = models.CharField(max_length=100)
    field_4 = models.CharField(max_length=100)
    field_5 = models.CharField(max_length=100)
    field_6 = models.CharField(max_length=100)
    field_7 = models.CharField(max_length=100)
    field_8 = models.CharField(max_length=100)
    field_9 = models.CharField(max_length=100)
    field_10 = models.CharField(max_length=100)













