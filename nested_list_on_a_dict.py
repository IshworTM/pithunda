n = int(input())
marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    marks[name] = scores
check = input()

if check in marks:
    avg = sum(marks[check]) / len(marks[check])
    print(f"{avg:.2f}")
else:
    print(f"Error 303: No student found with that name.")