grade_dict = {
    "s": 10,
    "a": 9,
    "b": 8,
    "c": 7,
    "d": 6,
    "e": 5
}

# ----------- user input ---------------
# print("Enter the number of credits followed by the grade:")
# credits = []
# grades = []
# while True:
#     c = float(input("Course credits: "))
#     if c == 0:
#         break
#     g = input("Course Grade: ").lower()
#     credits.append(c)
#     grades.append(g)



# ----------- hardcoded ---------------
courses = [
    (3, 'a'),   # Embedded Theory
    (1.5, 's'), # STS
    (3, 's'),   # Crypto Theory
    (2, 'a'),   # CPS Theory
    (3, 'a'),   # AI Theory
    (3, 'a'),   # Compiler Theory
    (3, 'a'),   # ML Theory
    (1, 's'),   # Crypto LAB
    (1, 's'),   # CPS LAB
    (1, 's'),   # Compiler LAB
    (1, 's')    # ML LAB
]
credits = list(c for c, _ in courses)
grades = list(g for _, g in courses)


# --------------------------------------------------------------------

total_credits = sum(credits)
total_GP = 0.0

for credit, grade in zip(credits, grades):
    temp_G = credit * grade_dict.get(grade, 0)
    total_GP += temp_G

GPA = total_GP / total_credits
print(f'Your GPA this sem: {GPA}')