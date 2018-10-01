from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^dashboard$', views.myChecklist, name='myChecklist'),
    # Get all Items associated with this user
    url(r'^all/$', views.myChecklist, name='myChecklist'),

    #Login
    url(r'^login/$', views.Login, name='Login'),
    #Logout
    url(r'^logout/$', views.Logout, name='Logout'),

    # Get all Items with the given category
    url(r'^category/(?P<category_name>\w+)$', views.itemsByCategory, name='itemsByCategory'),

    # Get the specified Item
    url(r'^(?P<item_id>[0-9]+)/$', views.getitem_byId, name='getitem_byId'),

    #Delete the Item
    url(r'^(?P<item_id>[0-9]+)/delete$', views.deleteItem, name='deleteItem'),

    #Complete the Item
    url(r'^(?P<item_id>[0-9]+)/complete$', views.completeItem, name='completeItem'),
    #Reopen the Item
    url(r'^(?P<item_id>[0-9]+)/reopen$', views.reopenItem, name='reopenItem'),
    #Edit The Item
    url(r'^(?P<item_id>[0-9]+)/edit$', views.editItmes, name='editItmes'),
    #Create Item
    url(r'^createItem$', views.createItem, name='createItem'),
]
