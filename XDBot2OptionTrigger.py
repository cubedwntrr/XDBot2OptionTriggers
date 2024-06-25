import os

print("NOTE: Make sure to create a file called level.txt with the decrypted and gunzipped level string or else this won't work!\n")

filename = input("Enter file name. Include the file format.\n")

macro = open(filename, "r")

data = macro.readlines()
macro.close()

if os.path.isfile("converted.txt") == False:
    cfile = open("converted.txt", "x")
    cfile.close() #create file if exists
else:
    os.remove("converted.txt") #else delete it

cfile = open("converted.txt", "a")

#Plain text conversion setup

print("Converting to plain text..")

for i in range(1, len(data)):
    line = data[i]
    line = line.strip("\n") #remove newlines
    inputdata = line.split("|")

    cfile.write(inputdata[5]) #Write player X-Pos
    cfile.write(" ")
    cfile.write(inputdata[1]) #Write hold or release input
    cfile.write(" ")
    if inputdata[3] == "1": #inputdata[3] is player
        cfile.write("0")
    if inputdata[3] == "0":
        cfile.write("1")
    cfile.write("\n")

print("\nDone!")

cfile.close()

cfile = open("converted.txt", "r")
macro = cfile.readlines()

delete = open("converted.txt", "w")
delete.write("") #remove everything in uncleaned file
delete.close()

cfile = open("converted.txt", "a")

athold = True

print("Cleaning inputs..")

for i in range(1, len(macro)):
    line = macro[i]
    if ("1 0" in line and athold == False or i == 1): #check for hold inputs. if a hold input is found, it stops writing lines until a release input is found
        holdline = i
        athold = True
        cfile.write(line)
    if "0 0" in line:
        cfile.write(line) #write input when release is found
        athold = False

print("\nDone!")

cfile.close()
        

inputs = open("converted.txt", "r")

file = open("level.txt", "a") #Decrypted and gunzipped level string

line = ""

print("Writing to decrypted level string..")

file.write("1,2899,2,-15,3,-15,155,1,36,1,165,1,199,1;")

for i in range(1, len(data)): #i wrote most of this code for another script like 3 months ago lmao
    line = inputs.readline()
    splitted = line.split(" ")
    if "1 0" in line: #Convert hold into option trigger
        line = line.replace(" 1 0\n", "")
        line.strip("\n")
        file.write("1,2899,2,"+splitted[0]+",3,-15,155,1,36,1,165,-1,199,-1;")
    if "0 0" in line: #Convert release into option trigger
        line = line.replace(" 0 0\n", "")
        line.strip("\n")
        file.write("1,2899,2,"+splitted[0]+",3,-15,155,1,36,1,165,1,199,1;")
file.close()

print("Done!")

input("Finished converting to option triggers. You may now close the program.")
