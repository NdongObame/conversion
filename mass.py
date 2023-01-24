def Mass():
    table = {1: "ton", 2: "quin tal", 3: ".", 4: "kilogram", 5: "hectogram", 6: "deca gram",
             7: "gram", 8: "deci gram", 9: "centigram", 10: "milligram"}
    print(table)
    U1 = int(input("you want to convert ? :"))
    U2 = int(input("into ? :"))
    value = int(input("how many " + table[U1] + " do you want to convert into " + table[U2] + " :"))
    if U1 == 1:
        converter = {1: 1, 2: 10, 3: 10 ** 2, 4: 10 ** 3, 5: 10 ** 4, 6: 10 ** 5, 7: 10 ** 6, 8: 10 ** 7, 9: 10 ** 8,
                     10: 10 ** 9}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 2:
        converter = {1: 0.1, 2: 1, 3: 10, 4: 10 ** 2, 5: 10 ** 3, 6: 10 ** 4, 7: 10 ** 5, 8: 10 ** 6, 9: 10 ** 7,
                     10: 10 ** 8}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 3:
        converter = {1: 0.01, 2: 0.1, 3: 1, 4: 10, 5: 10 ** 2, 6: 10 ** 3, 7: 10 ** 4, 8: 10 ** 5, 9: 10 ** 6,
                     10: 10 ** 7}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 4:
        converter = {1: 0.001, 2: 0.01, 3: 0.1, 4: 1, 5: 10, 6: 10 ** 2, 7: 10 ** 3, 8: 10 ** 4, 9: 10 ** 5,
                     10: 10 ** 6}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 5:
        converter = {1: 0.0001, 2: 0.001, 3: 0.01, 4: 0.1, 5: 1, 6: 10, 7: 10 ** 2, 8: 10 ** 3, 9: 10 ** 4,
                     10: 10 ** 5}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 6:
        converter = {1: 0.00001, 2: 0.0001, 3: 0.001, 4: 0.01, 5: 0.1, 6: 1, 7: 10, 8: 10 ** 2, 9: 10 ** 3,
                     10: 10 ** 4}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 7:
        converter = {1: 0.000001, 2: 0.00001, 3: 0.0001, 4: 0.001, 5: 0.01, 6: 0.1, 7: 1, 8: 10, 9: 10 ** 2,
                     10: 10 ** 3}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 8:
        converter = {1: 0.0000001, 2: 0.000001, 3: 0.00001, 4: 0.0001, 5: 0.001, 6: 0.01, 7: 0.1, 8: 1, 9: 10,
                     10: 10 ** 2}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 9:
        converter = {1: 0.00000001, 2: 0.0000001, 3: 0.000001, 4: 0.00001, 5: 0.0001, 6: 0.001, 7: 0.01, 8: 0.1, 9: 1,
                     10: 10}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])
    elif U1 == 10:
        converter = {1: 0.000000001, 2: 0.00000001, 3: 0.0000001, 4: 0.000001, 5: 0.00001,
                     6: 0.0001, 7: 0.001, 8: 0.01, 9: 0.1, 10: 1}
        convert = converter[U2]
        result = value * convert
        print(str(value) + " " + table[U1] + ", equals " + str(result) + " " + table[U2])