# Arthur LOUIS s191230
# November 15th, 2021

print("Simple Python to create control logic ROM file (week 4)")

f = open("4.0_control_logic", 'w')

f.write("v2.0 raw\n") # file version Logisim need to read

f.write("24*0 ")

f.write("a0 ")
f.write("c ")
f.write("6*0 ")

f.write("d0 ") # ADD
f.write("1d0 ") # SUB
f.write("2d0 ") # MUL
f.write("3d0\n") # DIV

f.write("7d0 ") # CMPEQ
f.write("8d0 ") # CMPLT
f.write("9d0 ") # CMPLE

f.write("0 ")

f.write("4d0 ") # AND
f.write("5d0 ") # OR
f.write("6d0 ") # XOR

f.write("0\n")

f.write("ad0 ") # SHL
f.write("bd0 ") # SHR
f.write("cd0 ") # SRA

f.write("0 ")

f.write("90 ") # ADDC
f.write("190 ") # SUBC
f.write("290 ") # MULC
f.write("390\n") # DIVC

f.write("790 ") # CMPEQC
f.write("890 ") # CMPLTC
f.write("990 ") # CMPLEC

f.write("0 ")

f.write("490 ") # ANDC
f.write("590 ") # ORC
f.write("690 ") # XORC

f.write("0\n")

f.write("a90 ") # SHLC
f.write("b90 ") # SHRC
f.write("c90 ") # SRAC

print("\nScript went well")