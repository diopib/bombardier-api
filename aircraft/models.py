from django.db import models

# Create your models here.

class Aircraft(models.Model):
    date_completed = models.CharField(max_length=256, null=True, blank=True)
    manufacturer = models.CharField(max_length=256, null=True, blank=True)
    model = models.CharField(max_length=256, null=True, blank=True)
    physical_class = models.CharField(max_length=256, null=True, blank=True)
    nb_engines = models.CharField(max_length=256, null=True, blank=True)
    aac = models.CharField(max_length=256, null=True, blank=True)
    adg = models.CharField(max_length=256, null=True, blank=True)
    tdg = models.CharField(max_length=256, null=True, blank=True)
    approach_speed = models.CharField(max_length=256, null=True, blank=True)
    wingtip_config = models.CharField(max_length=256, null=True, blank=True)
    wingspan = models.CharField(max_length=256, null=True, blank=True)
    length = models.CharField(max_length=256, null=True, blank=True)
    tail_height = models.CharField(max_length=256, null=True, blank=True)
    wheel_base = models.CharField(max_length=256, null=True, blank=True)
    cmg = models.CharField(max_length=256, null=True, blank=True)
    mgw = models.CharField(max_length=256, null=True, blank=True)
    mtow = models.CharField(max_length=256, null=True, blank=True)
    max_ramp = models.CharField(max_length=256, null=True, blank=True)
    main_gear_config = models.CharField(max_length=256, null=True, blank=True)
    icao_code = models.CharField(max_length=256, null=True, blank=True)
    wake_category = models.CharField(max_length=256, null=True, blank=True)
    atct_weight_class = models.CharField(max_length=256, null=True, blank=True)
    years_manufactured = models.CharField(max_length=256, null=True, blank=True)
    notes = models.CharField(max_length=256, null=True, blank=True)
    tags = models.CharField(max_length=256, null=True, blank=True)
    
