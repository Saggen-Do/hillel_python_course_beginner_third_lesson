print("Enter your name.")
user_name = input("My name is ")
print("Enter your gender(Male or Female).")
user_gender = input("My gender is ")
print("Enter your age.")
user_age = int(input("My age is "))
if user_name == "admin":
    print("Greetings, Lord Vaider!")
elif user_name == "Guido":
    print("Thanks a lot!")
elif user_name == "Jack":
    print("I advice you to watch 'TENET'")
if 10<user_age< 14 and user_gender == "Male" or user_age>30 and user_gender == "Male":
    print("I advice you to watch", end=' ')
    print("Star Wars", "Mandalorian", sep = ' or ')
elif user_age<=11 and user_gender == "Male":
    print("I advice you to watch 'TMNT'")
elif user_age<16 and user_gender == "Female":
    print("I advice you to watch 'Insurgent'")
elif 22<user_age<32 and user_gender == "Female":
    print("I advice you to watch 'Transformers'")
else:
    print("Look at yourself!")