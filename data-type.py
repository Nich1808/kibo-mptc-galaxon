telemetry_line = "Status: OK | ID: 4 | Margin: LV3"
fields = telemetry_line.split('|')

status = fields[0].split(':')[1]

print(status)