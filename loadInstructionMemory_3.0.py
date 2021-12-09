# Arthur LOUIS s191230
# November 5th, 2021

print("Simple Python to create control logic ROM file")

f = open("3.0_instruction_memory", 'w')

f.write("v2.0 raw\n") # file version Logisim need to read

f.write("0 ")

f.write("80611000 ") # ADD
f.write("84611000 ") # SUB
f.write("88611000 ") # MUL
f.write("8c611000 ") # DIV

f.write("c0610002 ") # ADDC
f.write("c4610002 ") # SUBC
f.write("c8610002\n") # MULC
f.write("cc610002 ") # DIVC

f.write("a9611000 ") # AND
f.write("a4611000 ") # OR
f.write("a8611000 ") # XOR

f.write("e0610002 ") # ANDC
f.write("e4610002 ") # ORC
f.write("e8610002 ") # XORC

f.write("90611000\n") # CMPEQ 
f.write("94611000 ") # CMPLT
f.write("98611000 ") # CMPLE

f.write("d0610002 ")  # CMPEQC
f.write("d4610002 ") # CMPLTC
f.write("d8610002 ") # CMPLEC

f.write("b0611000 ") # SHL
f.write("b4611000 ") # SHR
f.write("b8611000\n") # SRA

f.write("f0610002 ") # SHLC
f.write("f4610002 ") # SHRC
f.write("f8610002") # SRAC

print("\nScript went well")