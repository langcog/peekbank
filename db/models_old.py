from __future__ import unicode_literals

from django.db.models import Model, CharField, ForeignKey, IntegerField, DateField, TextField, FloatField, BooleanField
from datetime import datetime

class AOI_Coordinate_Record(Model):
    aoi_coordinates_id = IntegerField(blank=True, null=False, default=None)
    l_x_min = IntegerField(blank=True, null=True, default=None)
    l_x_max = IntegerField(blank=True, null=True, default=None)
    l_y_min = IntegerField(blank=True, null=True, default=None)
    l_y_max = IntegerField(blank=True, null=True, default=None)

    class Meta:
        app_label = 'db'
        db_table = 'aoi_coordinates'


class Dataset_Record(Model):
    dataset_id = IntegerField(blank=True, null=False, default=None)
    tracker = IntegerField(blank=True, null=True, default=None)
    monitor_size_x = IntegerField(blank=True, null=True, default=None)
    monitor_size_y = IntegerField(blank=True, null=True, default=None)
    sample_rate = IntegerField(blank=True, null=True, default=None)

    class Meta:
        app_label = 'db'
        db_table = 'datasets'

class Subject_Record(Model):
    subject_id = IntegerField(blank=True, null=True, default=None)
    age = IntegerField(blank=True, null=True, default=None)    
    sex = CharField(max_length=255, blank=True, default=None, null=True) 

    class Meta:
        app_label = 'db'
        db_table = 'subjects'

class Trial_Record(Model):    
    #dataset = ForeignKey(Dataset_Record, blank=True, null=True, default=None)
    trial_id = IntegerField(blank=True, null=False, default=None)
    dataset_id = IntegerField(blank=True, null=False, default=None)
    target_side = CharField(max_length=255, blank=True, default=None, null=True) 
    target_label = CharField(max_length=255, blank=True, default=None, null=True) 
    distractor_label = CharField(max_length=255, blank=True, default=None, null=True) 
    target_image = CharField(max_length=255, blank=True, default=None, null=True) 
    distractor_image = CharField(max_length=255, blank=True, default=None, null=True) 
    full_phase = IntegerField(blank=True, null=True, default=None)
    point_of_disambiguation = IntegerField(blank=True, null=True, default=None)

    class Meta:
        app_label = 'db'
        db_table = 'trials'


class AOI_Data_Record(Model):
    #subject = ForeignKey(Subject_Record, blank=True, null=True, default=None)
    subject_id = IntegerField(blank=True, null=False, default=None)
    t = IntegerField(blank=True, null=True, default=None)
    aoi = CharField(max_length=255, blank=True, default=None, null=True) #!!! SM: revisit FK
    trial = IntegerField(blank=True, null=False, default=None)

    class Meta:
        app_label = 'db'
        db_table = 'aoi_data'

class XY_Data_Record(Model):    
    x = IntegerField(blank=True, null=True, default=None)
    y = IntegerField(blank=True, null=True, default=None)
    #trial = ForeignKey(Trial_Record, blank=True, null=True, default=None)
    trial_id = IntegerField(blank=True, null=False, default=None)
    #subject = ForeignKey(Subject_Record, blank=True, null=True, default=None)
    subject_id = IntegerField(blank=True, null=False, default=None)

    class Meta:
        app_label = 'db'
        db_table = 'trials'

class Admin(Model):    
    admin_id = IntegerField(blank=True, null=True, default=None)
    date = DateField(max_length=255, blank=True, default=datetime.now, null=True)
    version = CharField(max_length=255, blank=True, default=None, null=True)

    class Meta:
        app_label = 'db'
        db_table = 'admin'


