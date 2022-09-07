# ERPNext related configs
ERPNEXT_API_KEY = '2abde2fd15990b1'
ERPNEXT_API_SECRET = '054fa4f8d90a182'
ERPNEXT_URL = '172.16.10.14'


# operational configs
PULL_FREQUENCY = 5 or 60  # in minutes
LOGS_DIRECTORY = 'logs'  # logs of this script is stored in this directory
IMPORT_START_DATE = '20220101' or None  # format: '20190501'

# Biometric device configs (all keys mandatory)
# - device_id - must be unique, strictly alphanumerical chars only. no space allowed.
# - ip - device IP Address
#- punch_direction - 'IN'/'OUT'/'AUTO'/None
# - clear_from_device_on_fetch: if set to true then attendance is deleted after fetch is successful.
# (Caution: this feature can lead to data loss if used carelessly.)
# devices = [
#     {"device_id": "HQ1", "ip": "172.16.20.51",
#         "punch_direction": 'AUTO', "clear_from_device_on_fetch": False},
#     {"device_id": "HQ2", "ip": "172.16.20.51",
#         "punch_direction": 'AUTO', "clear_from_device_on_fetch": False}
# ]
devices = [
    {"device_id": "HQ1", "ip": "172.16.20.51",
        "punch_direction": 'AUTO', "clear_from_device_on_fetch": False}
]

# Configs updating sync timestamp in the Shift Type DocType
shift_type_device_mapping = [
    {"shift_type_name": "NormalShift", "related_device_id": ["HQ1"]},
    {"shift_type_name": "NormalShift2", "related_device_id": ["HQ2"]
     }
]
