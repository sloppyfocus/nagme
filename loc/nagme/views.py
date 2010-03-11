from django.template import Context, loader
from site.nagme.models import Contact
from django.db.models.manager import Manager

def fill_contacts_context(d):
    fields = set(('contact_name', 'alias', 'contactgroups',
            'host_notifications_enabled', 'service_notifications_enabled',
            'host_notification_period', 'service_notification_period',
            'host_notification_options', 'service_notification_options',
            'host_notification_commands', 'service_notification_commands',
            'email', 'pager', 'can_submit_commands',
            'retain_status_information', 'retain_nonstatus_information'))
    contacts_list = []
    for contact in Contact.objects.all():
        contact_dict = {}
        contact_fields = set(dir(contact))
        for attribute in fields & contact_fields:
            attribute_object = getattr(contact, attribute)
            if isinstance(attribute_object, unicode):
                contact_dict[attribute] = attribute_object
            elif isinstance(attribute_object, bool):
                contact_dict[attribute] = '1' if attribute_object else '0'
            elif isinstance(attribute_object, Manager):
                contact_dict[attribute] = ','.join(unicode(x) for x in attribute_object.all())
        contacts_list.append(contact_dict)
    d['contacts_list'] = contacts_list
                
    

def contacts(request):
    t = loader.get_template('contacts.tmpl')
    Contact.objects.all()
    c = Context({
    })
    return t.render(c)
    
    
