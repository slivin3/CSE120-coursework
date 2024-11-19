##Created by SAL on 11/18/2024

print("Lets calculate the current in a circuit using Ohm's law!")

#Resistor inputs

##print("How many resisters are in this circuit? ")
## insert  logic here for looping the resistor input based on number of resistors.
R1 = float(input("Enter R1 value in Ohms: "))
print("R1 set to:", R1)
R2 = float(input("Enter R2 value in Ohms: "))
print("R2 set to:", R2)

#Voltage inputs
V1 = float(input("Enter Voltage value: "))
print(V1, "Volts")

#Resistor connection type set
ResistorConnectionType = input("Enter connection type: Series  or  Parallel: ")
if ResistorConnectionType =="Series":
    print("S type circuit")
    Rtotal = R1 + R2
    print("Total resistance: ", Rtotal)
elif ResistorConnectionType =="Parallel":
    print("P type circuit")
    Rtotal = 1 / ((1/R1) + (1/R2))
    print("Total resistance: ", Rtotal)
else:
    print("unknown circuit type")

#Current calculations using Ohm's Law
#V=I*R
#R=V/I
#I=V/R

C1 = V1 / Rtotal
print("Current is: ", C1,"Amps")
