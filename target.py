credits = [19.5, 18.5, 28.5, 22.5]
grades = [8.0, 9.0, 9.47, 9.16]

trial = 0.00

for i, j in zip(credits, grades):
    mul = i*j
    trial += mul

curr_credits = float(input("Enter current sem credits: "))
total_prev_credits = sum(credits)

total_credits = total_prev_credits + curr_credits

target = (9.10*total_credits) - trial

target /= curr_credits

print(target)