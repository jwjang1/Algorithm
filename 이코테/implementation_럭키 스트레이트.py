n = list(map(int, input()))

half = int(len(n)/2)
left_sum = sum(n[0:half])
right_sum = sum(n[half::])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")