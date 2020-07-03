import subprocess

from django.db import models

# Create your models here.


class Short_Url(models.Model):
    short_url = models.CharField(max_length=20)
    long_url = models.URLField("URL", unique=True)

    def copy2clip(self, txt):
        cmd = 'echo ' + (txt + self.short_url).strip() + '|pbcopy'
        return subprocess.check_call(cmd, shell=True)
