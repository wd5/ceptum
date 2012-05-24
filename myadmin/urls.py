from django.conf.urls.defaults import *

urlpatterns = patterns('',
                      url(r'^$', 'myadmin.views.auth', name="auth-page"),
                      url(r'^logout/$', 'myadmin.views.logout_view', name="logout-page"),
                      url(r'^clients/$', 'myadmin.views.clients', name="clients"),
                      url(r'^clients/all/$', 'myadmin.views.clients_all', name="clients_all"),
                      url(r'^clients/add$', 'myadmin.views.add_client', name="add_client"),
                      url(r'^clients/edit-ajx-client$', 'myadmin.views.edit_ajx_client', name="edit_ajx_client"),
                      url(r'^clients/edit/(?P<id>[-\w]+)/$', 'myadmin.views.edit_client', name="edit-client"),
                      url(r'^clients/del/(?P<id>[-\w]+)/$', 'myadmin.views.delete_client', name="delete-client"),
                      url(r'^clients/(?P<username>[-\w]+)/$', 'myadmin.views.user_clients', name="user-clients"),
                      url(r'^clients/page/(?P<id>[-\w]+)/$', 'myadmin.views.client_page', name="client_page"),
                      url(r'^change_product_field/$', 'myadmin.views.change_product_field', name="change-field"),
                      url(r'^store/$', 'myadmin.views.store', name="store-page"),
                      url(r'^unstore/$', 'myadmin.views.unstore', name="store-page"),
                      url(r'^allstore/$', 'myadmin.views.allstore', name="store-page"),
                      url(r'^cold/$', 'myadmin.views.cold_choose_cat', name="cold-choose-cat"),
                      url(r'^cold/toclient/$', 'myadmin.views.cold_to_client', name="cold-to-client"),
                      url(r'^cold/edit-ajx-target$', 'myadmin.views.edit_ajx_target', name="edit_ajx_target"),
                      url(r'^cold/send-ajx-mail$', 'myadmin.views.send_ajx_mail', name="send-ajx-mail"),
                      url(r'^cold/recalls-today/$', 'myadmin.views.recalls_today', name="recalls-today"),
                      url(r'^cold/stats/$', 'myadmin.views.cold_stats', name="cold-stats"),
                      url(r'^cold/unavailable/(?P<target_id>[-\w]+)/$', 'myadmin.views.cold_unavailable', name="cold-unavailable"),
                      url(r'^cold/(?P<category_id>[-\w]+)/$', 'myadmin.views.cold_start', name="cold-start"),
                      url(r'^cold/(?P<category_id>[-\w]+)/editmail/$', 'myadmin.views.cold_edit_mail', name="cold-edit-mail"),)

