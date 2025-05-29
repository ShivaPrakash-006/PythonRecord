principal = float(input("Enter Principal Amount (Rs.): "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time in Years: "))

interest = (principal * rate * time)/100
print("Amount after", time, "years:", principal + interest)
