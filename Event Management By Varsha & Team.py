print('welcome to Tech Fest 2022!')
print("Registrations open Now!!!")
i=int(input("Tap 1 for Events Schedule: "))
if i==1:
     print('''                         DAY-1
            Events:                   Time:       Entry Fee:   
            1.Drone Race              11:00am     Rs.600/-
            2.Hacker Series           12:00PM     Rs.150/- 
            3.Chat bot development    02:00PM     Rs.400/-
            4.Fast Service            02:00PM     Rs.300/-            
                                        DAY-2
            Events:                   Time:       Entry Fee: 
            1.Full throttle           02:00PM     Rs.600/-  
            2.Liftoff                 02:00PM     Rs.250/- 
            3.Ethical Hacking         02:00PM     Rs.400/-
            4.Arduino                 02:00PM     Rs.600/-                                       
             ''')
day=int(input("Tap 1 to register for Day-1 Events & 2 to Register for Day-2 Events: "))
if day==1:
    event=int(input("Enter choice of your event: "))
    if event==1:
        print("Welcome to Drone Race Registration!!!")
        i=int(input("Enter Number of participants"))
        for a in range(i):
            USN=str(input("Enter participant USN: "))
            Name=str(input("Enter participant Name: "))
            Email_ID=str(input("Enter participant Email: "))
        
    elif event==2:
        print("Welcome to Hacker Series Registration!!!")
        i=int(input("Enter Number of participants"))
        for a in range(i):
            USN=str(input("Enter participant USN: "))
            Name=str(input("Enter participant Name: "))
            Email_ID=str(input("Enter participant Email: "))
            
    elif event==3:
        print("Welcome to Chat Box Development Registration!!!")
        i=int(input("Enter Number of participants"))
        for a in range(i):
            USN=str(input("Enter participant USN: "))
            Name=str(input("Enter participant Name: "))
            Email_ID=str(input("Enter participant Email: "))
            
    elif event==4:
        print("Welcome to Fast Service Registration!!!")
        i=int(input("Enter Number of participants"))
        for a in range(i):
            USN=str(input("Enter participant USN: "))
            Name=str(input("Enter participant Name: "))
            Email_ID=str(input("Enter participant Email: "))
    
    else:
        print('Please enter a Valid option!')

elif day==2:
    event=int(input("Enter choice of your event: "))
    if event==1:
        print("Welcome to Full Throttle Registration!!!")
        i=int(input("Enter Number of participants"))
        for a in range(i):
            USN=str(input("Enter participant USN: "))
            Name=str(input("Enter participant Name: "))
            Email_ID=str(input("Enter participant Email: "))
        
    elif event==2:
        print("Welcome to Liftoff Registration!!!")
        i=int(input("Enter Number of participants"))
        for a in range(i):
            USN=str(input("Enter participant USN: "))
            Name=str(input("Enter participant Name: "))
            Email_ID=str(input("Enter participant Email: "))
            
    elif event==3:
        print("Welcome to Ethical Hacking Registration!!!")
        i=int(input("Enter Number of participants: "))
        for a in range(i):
            USN=str(input("Enter participant USN: "))
            Name=str(input("Enter participant Name: "))
            Email_ID=str(input("Enter participant Email: "))
            
    elif event==4:
        print("Welcome to Arduino Registration!!!")
        i=int(input("Enter Number of participants"))
        for a in range(i):
            USN=str(input("Enter participant USN: "))
            Name=str(input("Enter participant Name: "))
            Email_ID=str(input("Enter participant Email: "))

else:
        print('Please enter a Valid option!')

            





