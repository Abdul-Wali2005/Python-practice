
w = 0.0
learning_rate = 0.4

for step in range(1, 9):
    gradient = 2 * (w - 3)
    w = w - learning_rate * gradient
    print(step, round(w, 4))
