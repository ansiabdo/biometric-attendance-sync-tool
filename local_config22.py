
# ERPNext related configs
ERPNEXT_API_KEY = '2abde2fd15990b1'
ERPNEXT_API_SECRET = '054fa4f8d90a182'
ERPNEXT_URL = 'http://172.16.10.14'


# operational configs
PULL_FREQUENCY = 60 # in minutes
LOGS_DIRECTORY = 'logs_2022' # logs of this script is stored in this directory
IMPORT_START_DATE = '20220101' # format: '20190501'

# Biometric device configs (all keys mandatory)
    #- device_id - must be unique, strictly alphanumerical chars only. no space allowed.
    #- ip - device IP Address
    #- punch_direction - 'IN'/'OUT'/'AUTO'/None
    #- clear_from_device_on_fetch: if set to true then attendance is deleted after fetch is successful.
    #(Caution: this feature can lead to data loss if used carelessly.)
# devices = [
#     {'device_id':'test_1','ip':'192.168.0.209', 'punch_direction': None, 'clear_from_device_on_fetch': False},
#     {'device_id':'test_2','ip':'192.168.2.209', 'punch_direction': None, 'clear_from_device_on_fetch': False}
# ]

devices = [
    {'device_id': 'HQ', 'ip': '172.16.20.51','punch_direction': None, 'clear_from_device_on_fetch': False},
    {'device_id': 'Haddah', 'ip': '172.16.20.50','punch_direction': None, 'clear_from_device_on_fetch': False}
]


# Configs updating sync timestamp in the Shift Type DocType 
# please, read this thread to know why this is necessary https://discuss.erpnext.com/t/v-12-hr-auto-attendance-purpose-of-last-sync-of-checkin-in-shift-type/52997
# shift_type_device_mapping = [
#     {'shift_type_name': ['Shift1'], 'related_device_id': ['test_1','test_2']}
# ]

shift_type_device_mapping = [
    {'shift_type_name': ['NormalShift'], 'related_device_id': ['HQ', 'Haddah']}
]

# Ignore following exceptions thrown by ERPNext and continue importing punch logs.
# Note: All other exceptions will halt the punch log import to erpnext.
#       1. No Employee found for the given employee User ID in the Biometric device.
#       2. Employee is inactive for the given employee User ID in the Biometric device.
#       3. Duplicate Employee Checkin found. (This exception can happen if you have cleared the logs/status.json of this script)
# Use the corresponding number to ignore the above exceptions. (Default: Ignores all the listed exceptions)
allowed_exceptions = [1,2,3]