n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
numbers[0:3], numbers[3:6] = numbers[3:6], numbers[0:3]
print(' '.join(str(x) for x in numbers))
