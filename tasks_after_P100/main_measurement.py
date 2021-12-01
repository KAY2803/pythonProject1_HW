import logic_measurement

def measurement():
    while True:
        kind_of_measurement = str.upper(input('Выберите систему: T - температура, D - расстояние, W - масса '))
        if kind_of_measurement != 'T' and kind_of_measurement != 'D' and kind_of_measurement != 'W':
            print('только T, D или W (латинские)')
            continue
        if kind_of_measurement == 'T':
            print(logic_measurement.transfer_temperature())
        elif kind_of_measurement == 'D':
            print(logic_measurement.transfer_km_miles())
        else:
            print(logic_measurement.transfer_weight())
        return ''
print(measurement())