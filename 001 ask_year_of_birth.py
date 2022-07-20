from datetime import date
todays_date = int(date.today().year)
year_of_birth =""
while not year_of_birth.isdigit():
    print("Use numbers.")
    print("Enter your year of birth.")
    year_of_birth = input()
    if year_of_birth.isdigit():
        user_age = (todays_date-int(year_of_birth))
        if 21==user_age:
            print("You should visit Holland.")
        elif user_age>21:
            print("You should visit Vietnam.")
        else:
            print("Travell everywhere.")
        

    