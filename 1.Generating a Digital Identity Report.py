"""
Algorithm:
1. Collect the user's first name, last name, city, and job.
2. Remove leading and trailing spaces and capitalize each word.
3. Convert the birth year to an integer.
4. Create a digital identity using the first three letters of the first
   name, the first three letters of the last name, and the last two
   digits of the birth year.
5. Calculate the user's approximate age by subtracting the birth year
   from 2026.
6. Display a personalized report using an f-string.


Example Input:
First Name: Mohyaldin
Last Name: Amiri
City Name: Ardabil
Job: Python Developer
Birth Year: 1995

Example Output:
To create a digital identity for you, we need your information. Therefore, please enter the details requested below.

========== PERSONAL REPORT ==========

Hello Dear Mohyaldin Amiri

Based on the information you entered, you were born in 1995 and are 31 years old.
You also live in the city of Ardabil and work as a Python Developer.

Based on our algorithms, the best virtual identity for you could be: MohAmi95

Good Luck
"""

#user's initial message
print("To create a digital identity for you, we need your information. Therefore, please enter the details requested below.")


#Getting input from the user and assigning it to variables
FirstName = input("Your First Name: ").strip().title()
LastName = input("Your Last Name: ").strip().title()
CityName = input("Your City Name: ").strip().title()
Job = input("Your Job: ").strip().title()
BirthYear = int(input("Your Birth Year: "))

#Creating a digital identity based on the provided information
DigitalIdentity = f"{FirstName[:3]}{LastName[:3]}{str(BirthYear)[-2:]}"


#Final output
FinalOutput = f"""

                    ========== PERSONAL REPORT ==========

    Hello Dear {FirstName} {LastName} 

    Based on the information you entered, you were born in {BirthYear} and are {2026 - BirthYear} years old
    You also live in the city of {CityName} and work as a {Job}

    Based on our algorithms, the best virtual identity for you could be: {DigitalIdentity}
    
    Good Luck 
"""
print(FinalOutput)


