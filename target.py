credits = [19.5, 18.5, 28.5, 22.5]
grades = [8.0, 9.0, 9.47, 9.16]

trial = 0.00

for i, j in zip(credits, grades):
    mul = i*j
    trial += mul

curr_credits = float(input("Enter current sem credits: "))
final_target = float(input("Enter how much you wish in the final: "))
total_prev_credits = sum(credits)

total_credits = total_prev_credits + curr_credits

target = (final_target*total_credits) - trial

target /= curr_credits

# sem5 = 23.5

print(target)