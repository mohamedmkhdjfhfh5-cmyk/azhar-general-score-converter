print("1 - Azhar to General")
print("2 - General to Azhar")

choice = input("Choose: ")

if choice == "1":
    azhar_score = float(input("Enter Azhar Score: "))
    general_score = (azhar_score / 510) * 280
    print("Equivalent General Score =", general_score)

if choice == "2":
    school_score = float(input("Enter School Score: "))
    azhar_score = (school_score / 280) * 510
    print("Required Azhar Score =", azhar_score)
