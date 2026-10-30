from ncclient import manager

with manager.connect(
    host='192.168.56.11',
    port=830,
    username='admin',
    password='Cisco123!',
    hostkey_verify=False,
    device_params={'name': 'iosxe'},
) as m:
    caps = list(m.server_capabilities)
    print(f'Server advertises {len(caps)} capabilities')
    print([c for c in caps if 'ietf-interfaces' in c])
