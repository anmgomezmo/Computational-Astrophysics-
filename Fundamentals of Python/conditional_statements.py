import numpy as np

a = np.random.random()

if a < 0.5:
    print(f"a = {a:.6g} is < 0.5")
else:
    print(f"a = {a:.6g} is >= 0.5")

b = np.random.random()

if a <= 0.3:
    print(f"a = {a:.5g} is <= 0.3")
elif a > 0.3 and a < 0.6:
    print(f"0.3 < a = {a:.5g} < 0.6")
else:
    print(f"a = {a:.5g} is >= 0.6")
