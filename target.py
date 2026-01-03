curr_credits = float(input("Enter current sem credits: "))
final_target = float(input("Enter target CGPA after current sem: "))

credits = [19.5, 18.5, 28.5, 22.5, 23.5]
grades = [8.0, 9.0, 9.47, 9.16, 9.32]

prev_GP = 0.00
prev_credits = sum(credits)

for credit, grade in zip(credits, grades):
    temp_GP = credit * grade
    prev_GP += temp_GP

total_credits = prev_credits + curr_credits
target_GP = final_target * total_credits 

target = (target_GP - prev_GP) / curr_credits

print(f'This sem: {target} GPA to get {final_target} CGPA by the end of sem.')