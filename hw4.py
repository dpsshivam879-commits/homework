# Prompt the user for input
user_input = input("How many terms of the Fibonacci sequence would you like? ")

# Convert the input string to an integer
n = int(user_input)

# Initialize the first two numbers
a, b = 0, 1

print(f"\nHere is your Fibonacci series for {n} terms:")

# Loop 'n' times
for _ in range(n):
    print(a, end=" ") # 'end=" "' keeps the output on one line
    a, b = b, a + b