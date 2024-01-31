def asteroid_collision(asteroids):
    stack = []
    for i in range(len(asteroids)):
        curr = asteroids[i]
        while stack and stack[-1] > 0 and curr < 0:
            if stack[-1] >= abs(curr):
                if stack[-1] == abs(curr):
                    stack.pop()
                break
            stack.pop()
        else:
            stack.append(curr)
    return stack

asteroids = list(map(int, input().split()))
result = asteroid_collision(asteroids)
print(result)