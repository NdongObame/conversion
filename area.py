def Area():
    table = {1: "Square kilometre(s)", 2: "square hectometre(s)/ hectare", 3: "square deca-meter(s)/acre",
             4: "square metre(s)", 5: "square decimetre(s)", 6: "square centimetre(s)", 7: "square millimetre(s)"}
    print(table)
    U1 = int(input("you want to convert ? :"))
    U2 = int(input("into ? :"))
    value = int(input("how many " + table[U1] + " do you want to convert into " + table[U2] + " :"))
    if U1 == 1:
        converter = {1: 1, 2: 100, 3: 100 ** 2, 4: 100 ** 3, 5: 100 ** 4, 6: 100 ** 5, 7: 100 ** 6}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 2:
        converter = {1: 00.1, 2: 1, 3: 100, 4: 100 ** 2, 5: 100 ** 3, 6: 100 ** 4, 7: 100 ** 5}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 3:
        converter = {1: 0.001, 2: 0.01, 3: 1, 4: 100, 5: 100 ** 2, 6: 100 ** 3, 7: 100 ** 4}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 4:
        converter = {1: 0.0001, 2: 0.001, 3: 0.01, 4: 1, 5: 100, 6: 100 ** 2, 7: 100 ** 3}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 5:
        converter = {1: 0.00001, 2: 0.0001, 3: 0.001, 4: 0.01, 5: 1, 6: 100, 7: 100 ** 2}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 6:
        converter = {1: 0.000001, 2: 0.00001, 3: 0.0001, 4: 0.001, 5: 0.01, 6: 1, 7: 100}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 7:
        converter = {1: 0.0000001, 2: 0.000001, 3: 0.00001, 4: 0.0001, 5: 0.001, 6: 0.01, 7: 1}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])