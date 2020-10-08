from django.db import models

# Create your models here.
class ProgramLanguage(models.Model):
    lang_id = models.AutoField
    lang_name = models.CharField(max_length=100,default="")
    lang_category = models.CharField(max_length=100, default="Individual")
    lang_short_desc = models.CharField(max_length=2500, default="")
    lang_brief_desc = models.TextField()
    lang_img = models.ImageField(upload_to="plm/images",default = "Individual")
    lang_saved = models.BooleanField(default=False)

    def __str__(self):
        return self.lang_name