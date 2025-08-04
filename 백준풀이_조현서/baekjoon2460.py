max_passengers = 0
current_passengers = 0

for i in range(0, 10):
    out_nums, in_nums = map(int, input().split())
    current_passengers += in_nums
    current_passengers -= out_nums
    
    max_passengers = max(max_passengers, current_passengers)

print(max_passengers)