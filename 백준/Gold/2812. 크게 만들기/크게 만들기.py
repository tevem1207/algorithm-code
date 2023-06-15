n, k = map(int, input().split())
num_arr = list(map(int, list(input())))
stack = []

for num in num_arr:
    if k:
        while k and stack and stack[-1] < num:
            stack.pop()
            k -= 1
    stack.append(num)

print("".join(map(str, stack[:len(stack) - k])))