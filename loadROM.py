# Arthur LOUIS s191230
# November 5th, 2021

print("Simple Python script to create a ROM file readable by Logisim\n")

filename = input("Please write the ROM filename : ")

f = open(filename, 'w')
f.write("v2.0 raw\n") # file version Logisim need to read

while(1):
    data = input("\nPlease write data for ROM (hexadecimal) or save to save file and exit script : ")
    if(data == "save"):
        f.close
        break
    else:
        i = input("Please write number of time you want this data in a row (decimal) : ")
        f.write(i + '*' + data + ' ') # expected syntax by Logisim