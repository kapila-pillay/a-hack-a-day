print("---ORAL HYGIENE---")

def care():
    if ch1==1:
        print("Routine tooth brushing is the principal method of preventing many oral diseases,\nand perhaps the most important activity an individual can practice to reduce plaque buildup.")
    elif ch==2:
        print("The tongue contains numerous bacteria which causes bad breath. Tongue cleaners are\n designed to remove the debris built up on the tongue. Using a toothbrush to clean the tongue \nis another possibility, however it might be hard to reach the back of the tongue and the bristles \nof the toothbrush may be too soft to remove the debris.")
    elif ch==3:
        print("Some dental professionals recommend subgingival irrigation, also known as water flossing, as a way to clean teeth and gums. ")
    else: print("Wrong choice!")

while True:
    print("Tell us what you wanna know about?")
    print("1. Source of problem disturbing hygiene\n2. Preventive Care\n3. Food and Drink\n4. Mouthwash")
    ch=int(input("Enter the serial number :"))
    print("-------------------------------------------------------------------------------------------")
    if ch==1:
        print("Source of problem in oral hygiene is:\nPlaque\nCalculus")
        print("-------------------------------------------------------------------------------------------")
    elif ch==2:
        print("1.Tooth Brushing\n2.Tongue Scrappers\n3.Oral irrigation")
        ch1=int(input("--To know more about enter the serial number :"))
        care()
        print("-------------------------------------------------------------------------------------------")
    elif ch==3:
        print("Eating a balanced diet and limiting sugar intake can help prevent tooth decay and periodontal disease.")
        print("Beneficial Foods: Milk, cheese, nuts, fatty fish, chicken, Green and black tea, etc")
        print("Harmful Foods   : Cooked starches, e.g. crisps/potato chips, chocolates, etc")
        print("-------------------------------------------------------------------------------------------")
    elif ch==4:
        print("There are three commonly used kinds of mouthwash\n1. Saline\n2. Essential oils\n3. Chlorhexidine gluconate.")
        print("-------------------------------------------------------------------------------------------")
    else: break
