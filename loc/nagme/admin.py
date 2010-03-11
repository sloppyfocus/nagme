import site.nagme.models 

import django
from django.contrib import admin
from django.conf.urls.defaults import patterns


for model in dir(site.nagme.models):
    obj = getattr(site.nagme.models, model)
    if model == 'Deploy':
        continue
    if isinstance(obj, django.db.models.base.ModelBase):
        admin.site.register(obj)


class DeployAdmin(admin.ModelAdmin):
    def deploy(self, blah):
        pass
        
    def get_urls(self):
        urls = super(self.__class__, self).get_urls()
        extra_urls = patterns('',
            (r'^deploy/$', self.admin_site.admin_view(self.deploy))
        )
        return extra_urls + urls

admin.site.register(site.nagme.models.Deploy, DeployAdmin)
