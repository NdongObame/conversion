def Volume():
    table = {1: "cubic metre(s)", 2: "cubic decimetre(s)", 3: "cubic centimeter(s)", 4: "cubic millimetre",
             5: "hectolitre(s)", 6: "deca-litre(s)", 7: "litre(s)", 8: "decilitre(s)",
             9: "centilitre(s)", 10: "millilitre(s)"}
    print(table)
    U1 = int(input("you want to convert ? :"))
    U2 = int(input("into ? :"))
    value = int(input("how many " + table[U1] + " do you want to convert into " + table[U2] + " :"))
    if U1 == 1:
        converter = {1: 1, 2: 1000, 3: 1000 ** 2, 4: 1000 ** 3,
                     5: 10, 6: 10 ** 2, 7: 10 ** 3, 8: 10 ** 4, 9: 10 ** 5, 10: 10 ** 6}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 2:
        converter = {1: 0.001, 2: 1, 3: 1000, 4: 1000 ** 2,
                     5: 0.01, 6: 0.1, 7: 1, 8: 10, 9: 10 ** 2, 10: 10 ** 3}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 3:
        converter = {1: 0.000001, 2: 0.001, 3: 1, 4: 1000,
                     5: 0.00001, 6: 0.0001, 7: 0.001, 8: 0.01, 9: 0.1, 10: 1}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 4:
        converter = {1: 0.000000001, 2: 0.000001, 3: 0.001, 4: 1,
                     5: 0.00000001, 6: 0.0000001, 7: 0.000001, 8: 0.00001, 9: 0.0001, 10: 0.001}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 5:
        converter = {1: 0.1, 2: 100, 3: 100 ** 2, 4: 100 ** 3,
                     5: 1, 6: 10, 7: 10 ** 2, 8: 10 ** 3, 9: 10 ** 4, 10: 10 ** 5}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 6:
        converter = {1: 0.01, 2: 10, 3: 100 ** 4, 4: 100 ** 7,
                     5: 0.1, 6: 1, 7: 10, 8: 10 ** 2, 9: 10 ** 3, 10: 10 ** 4}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 7:
        converter = {1: 0.001, 2: 1, 3: 1000, 4: 1000 ** 2,
                     5: 0.01, 6: 0.1, 7: 1, 8: 10, 9: 10 ** 2, 10: 10 ** 3}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 8:
        converter = {1: 0.0001, 2: 0.1, 3: 100, 4: 100000,
                     5: 0.001, 6: 0.01, 7: 0.1, 8: 1, 9: 10, 10: 10 ** 2}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 9:
        converter = {1: 0.00001, 2: 0.01, 3: 10, 4: 10000,
                     5: 0.0001, 6: 0.001, 7: 0.01, 8: 0.1, 9: 1, 10: 10}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 10:
        converter = {1: 0.000001, 2: 0.001, 3: 1, 4: 1000,
                     5: 0.00001, 6: 0.0001, 7: 0.001, 8: 0.01, 9: 0.1, 10: 1}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])