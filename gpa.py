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
    (3, 'a'),   # Controls Theory
    (3, 's'),   # Cloud Theory
    (3, 'a'),   # MGT Theory
    (1.5, 's'), # STS
    (3, 'a'),   # Prob Theory
    (3, 'a'),   # Software Theory
    (3, 'a'),   # DAA Theory
    (1, 's'),   # Prob LAB
    (1, 's'),   # Software LAB
    (1, 'a'),   # Controls LAB
    (1, 's')    # DAA LAB
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

# If cloud A - 9.191489361702128 - 9.017
# If cloud S - 9.319148936170214 - 9.044