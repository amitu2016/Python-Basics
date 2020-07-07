# Code starts here

# store variable names
P = 1000
r = 10
n = 2

# compound interest formula
A = P*(pow((1 + r/100),n))

# display compound interest
a =float(A)
print("%.2f"%a)

# display interest
interest = a - P
i = float(interest)
print("%.2f"%i)
# Code ends here
