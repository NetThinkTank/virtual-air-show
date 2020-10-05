from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField
from django.db import models

import virtual_air_show.settings as settings


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(null=False, blank=False, editable=False, auto_now_add=True)

    creator = models.ForeignKey(
        User, related_name='%(app_label)s_%(class)s_creator',
	null=False, blank=False, editable=False,
	on_delete=models.CASCADE
    )

    modified = models.DateTimeField(null=False, blank=False, editable=False, auto_now=True)

    modifier = models.ForeignKey(
        User, related_name='%(app_label)s_%(class)s_modifier',
        null=False, blank=False, editable=False,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return u'%s' % self.name


class PlaneModel(BaseModel):
    name = models.CharField(max_length=250, blank=False, null=False)
    slug = models.CharField(max_length=50, blank=False, null=False)

    plane_company_name = models.CharField(max_length=250, blank=False, null=False)
    plane_model_name = models.CharField(max_length=250, blank=False, null=False)

    description = models.TextField(blank=True, null=True)

    model_file = models.CharField(max_length=250, blank=False, null=False)


class Scene(BaseModel):
    name = models.CharField(max_length=250, blank=False, null=False)
    slug = models.CharField(max_length=50, blank=False, null=False)

    description = models.TextField(blank=True, null=True)


class Entity(BaseModel):
    scene = models.ForeignKey(Scene, blank=False, null=False)
    
    plane_model = models.ForeignKey(PlaneModel, blank=False, null=False)
    parameters = models.Textfield(blank=True, null=True)

    location_x = models.IntegerField(blank=False, null=False)
    location_y = models.IntegerField(blank=False, null=False)


class Clip(BaseModel):
    name = models.CharField(max_length=250, blank=False, null=False)
    slug = models.CharField(max_length=50, blank=False, null=False)
 
    plane_company_name = models.CharField(max_length=250, blank=True, null=True)
    plane_model_name = models.CharField(max_length=250, blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    location_text = models.CharField(max_length=250, blank=True, null=True)
    location_point = PointField(blank=False, null=False)

    clip_file = models.CharField(max_length=250, blank=False, null=False)

