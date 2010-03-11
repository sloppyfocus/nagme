from django.db import models

class Host(models.Model):
    host_name = None
    alias = None
    address = None
    parents = None
    hostgroups = None
    check_command = None
    max_check_attempts = None
    check_interval = None
    retry_interval = None
    check_period = None
    contacts = None
    contact_groups = None
    notification_interval = None
    notification_period = None
    notification_options = None

class HostGroup(models.Model):
    hostgroup_name = None
    alias = None
    members = None
    hostgroup_members = None

class Service(models.Model):
    host_name = None
    hostgroup_name = None
    service_description = None
    servicegroups = None
    check_command = None
    max_check_attempts = None
    check_interval = None
    retry_interval = None
    check_period = None
    notification_interval = None
    notification_period = None
    notification_options = None

class ServiceGroup(models.Model):
    servicegroup_name = None
    alias = None
    members = None
    servicegroup_members = None

class Contact(models.Model):
    contact_name = models.CharField(unique=True, max_length=30)
    alias = models.CharField(blank=True, max_length=140)
    contactgroups = models.ManyToManyField('ContactGroup', null=True, blank=True)
    host_notifications_enabled = models.BooleanField()
    service_notifications_enabled = models.BooleanField()
    host_notification_period = models.ForeignKey(
        'TimePeriod', related_name='host_notification_period_timeperiod_id')
    service_notification_period = models.ForeignKey(
        'TimePeriod', related_name='service_notification_period_timeperiod_id')
    host_notification_options = models.SmallIntegerField()
    service_notification_options = models.SmallIntegerField()
    host_notification_commands = models.ForeignKey(
        'Command', related_name='host_notification_command_id')
    service_notification_commands = models.ForeignKey(
        'Command', related_name='service_notification_command_id')
    email = models.EmailField(blank=True)
    pager = models.EmailField(blank=True)
    can_submit_commands = models.BooleanField()
    def __unicode__(self):
        return self.contact_name
    

class ContactGroup(models.Model):
    contactgroup_name = models.CharField(unique=True, max_length=30)
    alias = models.CharField(max_length=140)
    members = models.ManyToManyField('Contact', null=True, blank=True)
    contactgroup_members = models.ManyToManyField(
            'self', null=True, blank=True)
    def __unicode__(self):
        return self.contactgroup_name

class TimePeriod(models.Model):
    timeperiod_name = models.CharField(unique=True, max_length=50)
    alias = models.CharField(max_length=140)
    dateranges = models.ManyToManyField('DateRange', null=True, blank=True)
    exclude = models.ManyToManyField('self', null=True, blank=True)
    def __unicode__(self):
        return self.timeperiod_name

class DateRange(models.Model):
    daterange_name = models.CharField(unique=True, max_length=50)
    dayspec = models.CharField(unique=True, max_length=140)
    timerange = models.CharField(max_length=140)

class Command(models.Model):
    command_name = models.CharField(unique=True, max_length=80)
    command_line = models.TextField()
    def __unicode__(self):
        return self.command_name

class ServiceDependency(models.Model):
    dependent_host_name = None
    dependent_hostgroup_name = None
    dependent_service_description = None
    host_name = None
    hostgroup_name = None
    service_description = None
    execution_failure_criteria = None
    notification_failure_criteria = None
    dependency_period = None

class HostDependency(models.Model):
    dependent_host_name = None
    dependent_hostgroup_name = None
    host_name = None
    hostgroup_name = None
    inherits_parent = None
    execution_failure_criteria = None
    notification_failure_criteria = None
    dependency_period = None

class Deploy(models.Model): pass
