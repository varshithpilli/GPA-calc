# Make sure the order in credits and GPAs is maintained as it affects the final calculation.
# Example:
# list = [first_sem, second_sem, third_sem, .....]

# Credits of the previous semesters already stored in a list
credits = [19.5, 18.5, 28.5]
# GPAs of the previous semesters already stored in a list
grades = [8.0, 9.0, 9.47]

current_credits = float(input("Enter the current semester credits: "))
current_grades = float(input("Enter the current semester GPA: "))
total_prev_credits = sum(credits)
total_prev_grades = 0.0
for i,j in zip(credits, grades):
    total_prev_grades += i*j

total_credits = total_prev_credits + current_credits
total_grades = total_prev_grades + (current_credits*current_grades)

print(f' Your CGPS is : {total_grades/total_credits}')
