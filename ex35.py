phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for vals in phone_numbers.values():
    if vals[0] == '+':
        print('00' + str(vals[1:]))
