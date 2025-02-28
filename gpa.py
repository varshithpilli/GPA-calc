print("Enter the number of credits followed by the grade:")
credits = []
grades = []

grade_dict = {
    "s": 10,
    "a": 9,
    "b": 8,
    "c": 7,
    "d": 6,
    "e": 5
}

while True:
    c = float(input("Credits: "))
    if c == 0:
        break
    g = input("Grade: ").lower()
    credits.append(c)
    grades.append(g)

total_credits = sum(credits)
total_grade = 0.0

for credit, grade in zip(credits, grades):
    total_grade += credit * grade_dict.get(grade, 0)

print("Your GPA is:", total_grade / total_credits)
