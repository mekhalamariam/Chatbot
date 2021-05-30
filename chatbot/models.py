from django.db import models
from django.contrib import auth

class User(auth.models.User, auth.models.PermissionsMixin):
    age=models.IntegerField(null=False)

    def str(self):
        return "@{}".format(self.username)


class Message(models.Model):
    message = models.CharField(max_length=1024)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    writer=models.CharField(max_length= 20, default='bot')


class Reply(models.Model):
    reply_message=models.CharField(max_length=1024)
    def str(self):
        return str(self.reply_message)


class UserMessage(models.Model):
    user_message=models.CharField(max_length=1024)
    reply=models.ForeignKey(Reply, on_delete=models.CASCADE)
    def str(self):
        return str(self.user_message)







    



