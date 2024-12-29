def convertBinToHex(bin):
    hex = " "
    if bin == "0000":
        hex = "0"
    elif bin == "0001":
        hex = "1"
    elif bin == "0010":
        hex = "2"
    elif bin == "0011":
        hex = "3"
    elif bin == "0100":
        hex = "4"
    elif bin == "0101":
        hex = "5"
    elif bin == "0110":
        hex = "6"
    elif bin == "0111":
        hex = "7"
    elif bin == "1000":
        hex = "8"
    elif bin == "1001":
        hex = "9"
    elif bin == "1010":
        hex = "A"
    elif bin == "1011":
        hex = "B"
    elif bin == "1100":
        hex = "C"
    elif bin == "1101":
        hex = "D"
    elif bin == "1110":
        hex = "E"
    elif bin == "1111":
        hex = "F"
    return hex


def checkInstruction(inst):
    convertInstruction = " "
    if inst == "nop":
        convertInstruction = "0000"
    elif inst == "sw":
        convertInstruction = "0001"
    elif inst == "sub":
        convertInstruction = "0010"
    elif inst == "slt":
        convertInstruction = "0011"
    elif inst == "beq":
        convertInstruction = "0100"
    elif inst == "sll":
        convertInstruction = "0101"
    elif inst == "jmp":
        convertInstruction = "0110"
    elif inst == "add":
        convertInstruction = "0111"
    elif inst == "lw":
        convertInstruction = "1000"
    elif inst == "addi":
        convertInstruction = "1001"
    elif inst == "and":
        convertInstruction = "1010"
    else:
        convertInstruction = "Invalid instrcutions"
    return convertInstruction


def checkRegister(reg):
    convertReg = ""
    if reg == "r0":
        convertReg = "000"
    elif reg == "r1":
        convertReg = "001"
    elif reg == "r2":
        convertReg = "010"
    elif reg == "r3":
        convertReg = "011"
    elif reg == "r4":
        convertReg = "100"
    elif reg == "r5":
        convertReg = "101"
    elif reg == "r6":
        convertReg = "110"
    elif reg == "r7":
        convertReg = "111"

    else:
        convertReg == "Invalid Register"

    return convertReg


def decimalToBinary(num):
    if (num < 0):
        num = 13 + num

    ext = ""
    result = ""

    while (num > 0):
        if num % 2 == 0:
            result = "0" + result
        else:
            result = "1" + result
        # result = (num%2 == 0 ? "0" : "1") + result
        num = num // 2

    #for i in range(4 - len(result)):
        #ext = "0" + ext

    #result = ext + result

    return result


readf = open("inputs", "r")
writef = open("outputs", "w")
writef.write("v2.0 raw\n")

# print(f.readline())
for i in readf:
    splitted = i.split()

    if (splitted[0] == "add" or splitted[0] == "sub" or splitted[0] == "and" or splitted[0] == "slt" or splitted[0] == "nop"):
        conv_inst = checkInstruction(splitted[0])
        conv_rs = checkRegister(splitted[2])
        conv_rt = checkRegister(splitted[3])
        conv_rd = checkRegister(splitted[1])

        out = conv_inst + conv_rs + conv_rt + conv_rd
        print(out)


    elif (splitted[0] == "lw" or splitted[0] == "sw" or splitted[0] == "beq"  or splitted[
        0] == "addi"  or  splitted[0] == "sll" ):
        conv_inst = checkInstruction(splitted[0])
        conv_rs = checkRegister(splitted[2])
        conv_rt = checkRegister(splitted[1])
        conv_im = decimalToBinary(int(splitted[3]))
        if (len(conv_im) < 3):
            i = len(conv_im)
            while i < 3:
                conv_im = '0' + conv_im
                i += 1
        out = conv_inst + conv_rs + conv_rt + conv_im
        print(out)


    elif (splitted[0] == "jmp"):
        conv_inst = checkInstruction(splitted[0])
        conv_target =decimalToBinary(int(splitted[1]))
        if (len(conv_target) < 9):
            i = len(conv_target)
            while i < 9:
                conv_target = '0' + conv_target
                i += 1

                # targ = int(conv_target)
        # if targ < 9:
        out = conv_inst + "00" + conv_target
        # elif targ < 99:
        #    out = conv_inst + conv_target
        print(out)


    if (len(out) < 16):
        i = len(out)
        while i < 16:
            out = '0' + out
            i += 1

    i = 0
    hexa_decimal = ''
    while i < len(out):
        hexa_decimal = hexa_decimal + convertBinToHex(out[i: i + 4])
        i += 4

    writef.write(hexa_decimal+ "\n")