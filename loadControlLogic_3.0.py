# Arthur LOUIS s191230
# November 5th, 2021

print("Simple Python to create control logic ROM file")

f = open("3.0_control_logic", 'w')

f.write("v2.0 raw\n") # file version Logisim need to read

f.write("32*0 ")

f.write("c0 ") # ADD
f.write("1c0 ") # SUB
f.write("2c0 ") # MUL
f.write("3c0 ") # DIV

f.write("7c0 ") # CMPEQ
f.write("8c0 ") # CMPLT
f.write("9c0\n") # CMPLE

f.write("0 ")

f.write("4c0 ") # AND
f.write("5c0 ") # OR
f.write("6c0 ") # XOR

f.write("0 ")

f.write("ac0 ") # SHL
f.write("bc0 ") # SHR
f.write("cc0\n") # SRA

f.write("0 ")

f.write("80 ") # ADDC
f.write("180 ") # SUBC
f.write("280 ") # MULC
f.write("380 ") # DIVC

f.write("780 ") # CMPEQC
f.write("880 ") # CMPLTC
f.write("980\n") # CMPLEC

f.write("0 ")

f.write("480 ") # ANDC
f.write("580 ") # ORC
f.write("680 ") # XORC

f.write("0 ")

f.write("a80 ") # SHLC
f.write("b80 ") # SHRC
f.write("c80 ") # SRAC

print("\nScript went well")