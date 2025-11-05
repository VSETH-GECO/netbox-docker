# Add your plugins and plugin settings here.
# Of course uncomment this file out.

from os import environ

# To learn how to build images with your required plugins
# See https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins

# # Enable installed plugins. Add the name of each plugin to the list.
PLUGINS = [
    'netbox_napalm_plugin',
    'netbox_qrcode',
    'netbox_floorplan',
    'netbox_topology_views', 
    'netbox_inventory',
]

# # Plugins configuration settings. These settings are used by various plugins that the user may have installed.
# # Each key in the dictionary is the name of an installed plugin and its value is a dictionary of settings.


PLUGINS_CONFIG = {
    'netbox_napalm_plugin': {
        'NAPALM_USERNAME': 'napalmviewer',
        'NAPALM_PASSWORD': environ.get('NAPALM_PASSWORD', "dummyvalue"),
    },
}