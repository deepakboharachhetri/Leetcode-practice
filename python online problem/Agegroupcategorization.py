### Algorithm 
# step1: Get age from user 
# step2: check user group
        # 0-1 Years: Infant
        # 1-3 Years: Toddler
        # 3-12 Years: Child
        # 13-19 Years: Teenager / Adolescent
        # 20-39 Years: Young Adult
        # 40-74 Years: Adult / Middle-Aged
    # age ≥ 75
    # Senior Citizen / Elderly
# step3: print result


user_age=input("Enter your age:")
user_age_int=int(user_age)
if not(user_age_int >=0 and user_age_int <=150) :
    print("Invalid age \"age must under 0-150 \"")
    exit


if user_age_int < 1:
    print("Infant")
elif user_age_int < 3:
    print("Toddler")
elif user_age_int < 13:
    print("child")
elif user_age_int < 20:
    print("Teenager/Adolescent")

elif user_age_int <40:
    print("Young Adult")

elif user_age_int<75:
    print("Adult/Middle-Aged")

else:
    print("Senior citizen/Elderly")

