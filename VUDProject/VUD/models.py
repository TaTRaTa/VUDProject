from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cities(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name

class Clinics(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    
    class Meta:
        verbose_name_plural = "Clinics"

    def __str__(self):
        return self.name

class Status(models.Model):
    status = models.CharField(max_length=50)
    description = models.TextField(null=True)
    
    class Meta:
        verbose_name_plural = "Status"

    def __str__(self):
        return self.status

class HelpRequests(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='topics')
    title = models.SlugField()
    expected_ppl_cnt = models.PositiveSmallIntegerField(default=0)
    confirmed_ppl_cnt = models.PositiveSmallIntegerField(default=0)
    rejected_pll_cnt = models.PositiveSmallIntegerField(default=0)
    onhold_ppl_cnt = models.PositiveSmallIntegerField(default=0)
    valid_days = models.PositiveSmallIntegerField(default=7)
    isopen = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "HelpRequests"

    def __str__(self):
        return self.title

class HelpRequestsDetail(models.Model):
    postid = models.OneToOneField(HelpRequests, on_delete=models.CASCADE, primary_key=True, related_name='detail')
    description = models.TextField(max_length=500, null=True)
    phone = models.CharField(max_length=20, null=True)
    Facebook = models.URLField(null=True)
    instagram = models.URLField(null=True)
    email = models.URLField(null=True)
    clinics = models.ForeignKey(Clinics, null=True, blank=True, on_delete=models.CASCADE, related_name='topics')
    
    class Meta:
        verbose_name_plural = "HelpRequestsDetail"

    def __str__(self):
        return self.description

class HelpResponces(models.Model):
    topic = models.ForeignKey(HelpRequests, on_delete=models.CASCADE, related_name='replies')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    isValid = models.BooleanField(default=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='replies')
    
    class Meta:
        verbose_name_plural = "HelpResponces"

    def __str__(self):
        return ', '.join([str(self.topic), str(self.isValid), str(self.status)])
