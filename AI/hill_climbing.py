def f(x):
    return -x*x;

def hill_climbing(start):
    current=start;

    while True:
        left=current-1;
        right=current+1;
        current_val=f(current);
        left_val=f(left);
        right_val=f(right);

        print(f"current value: x={current},f(x):{current_val}");

        if left_val > current_val:
            current=left;

        elif right_val > current_val:
            current = right;

        else:
            print("\nSolution found!");
            print(f"Solution is: x = {current} , f(x) = {current_val}");
            return




start=int(input("Enter the starting value of x:"));

hill_climbing(start);

# Enter the starting value of x:3
# current value: x=3,f(x):-9
# current value: x=2,f(x):-4
# current value: x=1,f(x):-1
# current value: x=0,f(x):0

# Solution found!
# Solution is: x = 0 , f(x) = 0


import math

def f(x):
    return math.sin(x)


def hill_climbing(start):
    current = start

    while True:
        left = current - 0.1
        right = current + 0.1

        current_val = f(current)
        left_val = f(left)
        right_val = f(right)

        print(f"x={current:.2f}, f(x)={current_val:.4f}")

        if left_val > current_val:
            current = left
        elif right_val > current_val:
            current = right
        else:
            print("\nPeak reached!")
            print(f"x={current:.2f}, f(x)={current_val:.4f}")
            return


start = float(input("Enter starting value: "))
hill_climbing(start)