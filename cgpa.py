credits = [19.5, 18.5, 28.5]
grades = [8.0, 9.0, 9.47]

current_credits = float(input("Enter the credits: "))
current_grades = float(input("Enter the grades: "))
total_prev_credits = sum(credits)
total_prev_grades = 0.0
for i,j in zip(credits, grades):
    total_prev_grades += i*j

total_credits = total_prev_credits + current_credits
total_grades = total_prev_grades + (current_credits*current_grades)

print(total_grades/total_credits)