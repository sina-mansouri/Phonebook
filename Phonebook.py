from builtins import print


print( '''
   _   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ / \ 
 ( P | h | o | n | e | b | o | o | k )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
''')

print(" The Person and Number! ")

while True:

    NAME = input(" Please Enter Your Name? ")

    FAMILY = input(" Please Enter Your Family? ")

    print(" Hi " + NAME.lower() +" "+ FAMILY.lower())

    NUMBER = input( " Please Enter Your Mobile Number? ")

    with open("outputnumbers.txt", "a") as s:

        print(NAME.lower() + " " +FAMILY.lower() , file=s)
        print("Your Mobile Numbers is " + NUMBER , file=s)
        print("*********************************" , file=s)
    NEW = input(" Want You to continue?(y/n) ")
    if NEW == "y" :
        True
    elif NEW == "n" :
        print("END")
        break




