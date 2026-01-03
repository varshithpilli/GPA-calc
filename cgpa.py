curr_credits = float(input("Enter the current sem credits: "))
curr_GPA = float(input("Enter the current sem GPA: "))

credits = [19.5, 18.5, 28.5, 22.5, 23.5]
grades = [8.0, 9.0, 9.47, 9.16, 9.32]

prev_GP = 0.0
prev_credits = sum(credits)

for credit, grade in zip(credits, grades):
    temp_GP = credit * grade
    prev_GP += temp_GP

total_credits = prev_credits + curr_credits
total_GP = prev_GP + (curr_credits * curr_GPA)

CGPA = total_GP/total_credits

print(f'Your CGPA after this sem: {CGPA}')

# sem6 = 22.5