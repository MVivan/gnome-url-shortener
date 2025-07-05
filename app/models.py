from django.db import models
import string
import random

class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=6, unique=True, blank=True)
    clicks = models.IntegerField(default=0) 

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        chars = string.ascii_letters + string.digits
        while True:
            code = ''.join(random.choices(chars, k=6))
            if not ShortURL.objects.filter(short_code=code).exists():
                return code

    def get_short_url(self, request=None):
        domain = 'https://yourdomain.com'
        if request:
            domain = request.build_absolute_uri('/')[:-1]
        return f"{domain}/{self.short_code}"

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
