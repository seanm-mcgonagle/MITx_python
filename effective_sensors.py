def effective_sensors(b05, b06, b07):
    """
    The effective sensors function extracted from Davor's spreadsheet.
    See: https://confluence.carbonblack.local/x/ZSmuBQ for details.

    :param b05: The ratio of legacy sensors
    :param b06: Ingress rate in bytes
    :param b07: Event rate in operations per second
    """
    b09 = b06 / 10.0**7
    b10 = b07 / 41000.0
    return 18750.0 * (b09 + b10) * (1.0 + b05 / 2.0) / 2.0


sensor_ratio = 0
ingress_bytes = 100
ingress_events = 100

print(effective_sensors(sensor_ratio, ingress_bytes, ingress_events))
