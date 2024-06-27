# mixed = list(input())

# alphabets = []
# nums = []

# for i in range(len(mixed)):
#     try:
#         int(mixed[i])
#         nums.append(mixed[i])
#     except ValueError:
#         alphabets.append(mixed[i])

# number = list(map(int, nums))
# sum_num = sum(number[:])
# sum_num = str(sum_num)

# alphabets.sort()
# word = ''.join(alphabets)

# print(word+sum_num)

mixed = input()

alphabets = []
nums = []

for i in range(len(mixed)):
    if mixed[i].isdigit():
        nums.append(mixed[i])
    elif mixed[i].isalpha():
        alphabets.append(mixed[i])


number = list(map(int, nums))
sum_num = sum(number[:])
sum_num = str(sum_num)

alphabets.sort()
word = ''.join(alphabets)

print(word+sum_num)