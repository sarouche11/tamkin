from django.db import models
import random
# Create your models here.
def generate_code():
    return ''.join(random.choices('AZERTYUIOPQSDFGHJKLMWXCVBN123456789', k=10))

class MiclatData(models.Model):
    code = models.CharField(max_length=100, unique=True, default=generate_code)
    nin = models.CharField(max_length=18, unique=True, null=True, blank=True)
    sexe = models.CharField(max_length=10, null=True, blank=True)
    acteN = models.CharField(max_length=10, null=True, blank=True)
    annee = models.CharField(max_length=6, null=True, blank=True)
    nom_a = models.CharField(max_length=50, null=True, blank=True)
    nom_f = models.CharField(max_length=50, null=True, blank=True)
    d_nais = models.CharField(max_length=30, null=True, blank=True)
    h_nais = models.CharField(max_length=10, null=True, blank=True)
    pren_a = models.CharField(max_length=50, null=True, blank=True)
    pren_f = models.CharField(max_length=50, null=True, blank=True)
    presume = models.CharField(max_length=10, null=True, blank=True)
    codecomm = models.CharField(max_length=10, null=True, blank=True)
    nom_mere = models.CharField(max_length=50, null=True, blank=True)
    lieu_nais = models.CharField(max_length=50, null=True, blank=True)
    pren_mere = models.CharField(max_length=50, null=True, blank=True)
    pren_pere = models.CharField(max_length=50, null=True, blank=True)
    decesMentions = models.CharField(max_length=5, null=True, blank=True)
    divorceMentions = models.CharField(max_length=5, null=True, blank=True)
    mariageMentions = models.CharField(max_length=5, null=True, blank=True)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_in = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f" {self.nin}"
    
class MiclatLog(models.Model):
    STATUS_CHOICES = [
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
        ("ERROR", "Error"),
    ]
    code = models.CharField(max_length=100, unique=True, default=generate_code)
    nin = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    
    response_code = models.IntegerField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    response_data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_in = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f" {self.nin}"