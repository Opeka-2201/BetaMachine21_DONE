# Arthur LOUIS s191230
# November 18th, 2021

print("Simple Python to create control logic ROM file (week 5)")

f = open("5.0_control_logic", 'w')

f.write("v2.0 raw\n") # file version Logisim needs to read

f.write("24*0 ")
f.write("a0 ") # LD
f.write("c ") # ST
f.write("0 ")
f.write("82 ") # JMP
f.write("0 ")
f.write("80 ") # BEQ
f.write("80\n") # BNE

f.write("0 ")
f.write("d0 ") # ADD
f.write("1d0 ") # SUB
f.write("2d0 ") # MUL
f.write("3d0 ") # DIV
f.write("7d0 ") # CMPEQ
f.write("8d0 ") # CMPLT
f.write("9d0\n") # CMPLE

f.write("0 ")
f.write("4d0 ") # AND
f.write("5d0 ") # OR
f.write("6d0 ") # XOR
f.write("0 ")
f.write("ad0 ") # SHL
f.write("bd0 ") # SHR
f.write("cd0\n") # SRA

f.write("0 ")
f.write("90 ") # ADDC
f.write("190 ") # SUBC
f.write("290 ") # MULC
f.write("390 ") # DIVC
f.write("790 ") # CMPEQC
f.write("890 ") # CMPLTC
f.write("990\n") # CMPLEC

f.write("0 ")
f.write("490 ") # ANDC
f.write("590 ") # ORC
f.write("690 ") # XORC
f.write("0 ")
f.write("a90 ") # SHLC
f.write("b90 ") # SHRC
f.write("c90") # SRAC

f.close()

print("\nScript went well")