# -*- encoding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail, object_list
from scielomanager.journalmanager.models import *
from scielomanager.journalmanager.views import *


urlpatterns = patterns('',   
    # Journal Tools
    url(r'^$', journal_index, name="journal.index"),
    url(r'^add/$', add_journal, name='journal.add'),
    url(r'^show/(?P<journal_id>\d+)/$', show_journal, name='journal.show'),
    url(r'^edit/(?P<journal_id>\d+)/$', edit_journal, name='journal.edit'),    
    
    # Institution Tools
    url(r'^institution/$', institution_index, name='institution.index' ),
    url(r'^institution/add/$', add_institution, name='institution.add' ),
    url(r'^institution/show/(?P<institution_id>\d+)/$', show_institution, name='institution.show' ),    
    url(r'^institution/edit/(?P<institution_id>\d+)/$', edit_institution, name='institution.edit' ),
    
    # Users Tools
    url(r'^user/$', user_index, name="user.index"),
    url(r'^user/add/$', add_user, name="user.add"),
    url(r'^user/show/(?P<user_id>\d+)/$', show_user, name="user.show"),
    url(r'^user/edit/(?P<user_id>\d+)/$', edit_user, name="user.edit"),    

)