# Problem 2

prev_term = 1
curr_term = 2
sum = 0
limit = 4000000

while (curr_term < limit):
    if (curr_term % 2 == 0):
        sum += curr_term
    
    next_term = curr_term + prev_term
    prev_term = curr_term
    curr_term = next_term

print(sum)