x = float(input())
n = [0.0] * 100

n[0] = x
for i in range(1, 100):
    n[i] = n[i - 1] / 2

for i in range(100):
    print(f"N[{i}] = {n[i]:.4f}")
