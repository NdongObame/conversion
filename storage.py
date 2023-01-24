def Storage():
    table = {1: "byte(s)", 2: "kilobyte(s)", 3: "megabyte(s)", 4: "gigabyte(s)", 5: "terabyte(s)", 6: "petabyte(s)"}
    print(table)
    U1 = int(input("you want to convert ? :"))
    U2 = int(input("into ? :"))
    value = int(input("how many " + table[U1] + " do you want to convert into " + table[U2] + " :"))
    if U1 == 1:
        converter = {1: 1, 2: 0.001, 3: 0.000001, 4: 1.00000000e-9, 5: 1.00000000e-12, 6: 1.00000000e-15}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 2:
        converter = {1: 1000, 2: 1, 3: 0.001, 4: 0.000001, 5: 1.00000000e-9, 6: 1.00000000e-12}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 3:
        converter = {1: 1000 ** 2, 2: 1000, 3: 1, 4: 0.001, 5: 0.000001, 6: 1.00000000e-9}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 4:
        converter = {1: 1000 ** 3, 2: 1000 ** 2, 3: 1000, 4: 1, 5: 0.001, 6: 0.000001}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 5:
        converter = {1: 1000 ** 4, 2: 1000 ** 3, 3: 1000 ** 2, 4: 1000, 5: 1, 6: 0.001}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 6:
        converter = {1: 1000 ** 5, 2: 1000 ** 4, 3: 1000 ** 3, 4: 1000 ** 2, 5: 1000, 6: 1}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
