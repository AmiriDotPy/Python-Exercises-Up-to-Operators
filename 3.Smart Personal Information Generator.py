
"""
Algorithm:
Receive the first name, last name, birth year, and city.
Remove leading and trailing spaces and convert names and city to lowercase.
Calculate the lengths of the input strings, the user's age, next year's age, and completed decades.
Determine whether the birth year is even or odd using the modulo operator.
Create a User ID using string slicing.
Generate a password by reversing parts of the first name, last name, and city, then append their lengths.
Replace the reversed first four characters of the last name with a value calculated from the birth year and string lengths.
Determine the password length category, compare the name lengths, classify the age group, and print the report.

Example Input:
First Name: Mohyaldin
Last Name: Amiri
Birth Year: 1995
City: Ardabil

Example Output:
Generating a Digital Identity Report: 

------------------------------------------------
Full Name: Mohyaldin Amiri
Fname vs Lname: First name is Longer
Birth Year: 1995
Age: 31
Age Next Year: 32
Age Group: Young
Age Even Odd: Odd
Life Decades: 3
City: Ardabil
User ID: mohami95ar
User Password: yhom958951415365adra7
Password Security: ُStrong
------------------------------------------------
"""


print("Smart Personal Information Generator: ")
print("")
#ُStart - Receiving input and initializing variables
Fname = input("First Name: ").strip().lower()
Lname = input("Last Name: ").strip().lower()
BirthYear = int(input("Birth Year: "))
City = input("City: ").strip().lower() 
#End - Receiving input and initializing variables
print("")


#Start - Computations and Processing
FnameLen = len(Fname)
LnameLen = len(Lname)
CityLen = len(City)


AgeEvenOdd = "Even" if BirthYear % 2 == 0  else "Odd"
Age = 2026 - BirthYear 
AgeNextYear = Age + 1
LifeDecades = Age // 10
#End - Computations and Processing

#Start Create ID
UserID = f'{Fname[:3]}{Lname[:3]}{str(BirthYear)[-2:]}{City[:2]}'
#End Create ID
#Start Create Password
Password = f'{Fname[:4][::-1]}{FnameLen}{Lname[:4][::-1]}{LnameLen}{City[:4][::-1]}{CityLen}'
PasswordVerification = Lname[:4][::-1]
UserPassword = Password.replace(PasswordVerification , f'{str(BirthYear * 3)[::-1]}{CityLen *2}{LnameLen *3}{FnameLen *4}')
#End Create Password


#Start - Computations and Processing Continue
PasswordSecurity = "Strong" if len(UserPassword) > 8 else "Weak"
FnamevsLname = "First name is Longer" if FnameLen > LnameLen else "The lengths of both are equal" if FnameLen == LnameLen else "Last name is Longer"
AgeGroup = "Young" if Age < 35 else "Middle-aged" if  Age < 60 else "Elder"
#End - Computations and Processing Continue

print('------------------------------------------------')
print( "Full Name: " + Fname.title() + ' ' + Lname.title())
print( "Fname vs Lname: " + FnamevsLname)
print( "Birth Year: " + str(BirthYear))
print( "Age: " + str(Age))
print( "Age Next Year: " + str(AgeNextYear))
print( "Age Group: " + AgeGroup)
print( "Age Even Odd: " + AgeEvenOdd)
print( "Life Decades: " + str(LifeDecades))
print( "City: " + City.title())
print( "User ID: " + UserID)
print( "User Password: " + UserPassword)
print( "Password Security: " + PasswordSecurity)
print('------------------------------------------------')
