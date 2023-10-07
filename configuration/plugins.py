# Add your plugins and plugin settings here.
# Of course uncomment this file out.

password = "dummyvalue"
try:
    with open("/run/secrets/netbox/napalm_password", "r") as file:
        password = file.read().strip()
except Exception:
    pass


# To learn how to build images with your required plugins
# See https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins

PLUGINS = ["netbox_napalm_plugin"]

# PLUGINS_CONFIG = {
#   "netbox_bgp": {
#     ADD YOUR SETTINGS HERE
#   }
# }
PLUGINS_CONFIG = {
    'netbox_napalm_plugin': {
        'NAPALM_USERNAME': 'napalmviewer',
        'NAPALM_PASSWORD': password,
    },
}

