# Arthur LOUIS s191230
# November 15th, 2021

print("Simple Python to create control logic ROM file")

f = open("4.0_instruction_memory", 'w')

f.write("v2.0 raw\n") # file version Logisim need to read

f.write("0 ")
f.write("c03f0006 ")
f.write("c05f0003 ")
f.write("80611000 ")
f.write("647f0000 ")
f.write("64220009 ")
f.write("603f0000 ")
f.write("80611000\n")
f.write("647f0004 ")

print("\nScript went well")