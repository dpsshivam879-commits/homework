num = int(input("Enter a number: "))


original = num
temp = num


count = 0
while temp > 0:
    count = count + 1
    temp = temp // 10

 
temp = num
total = 0

while temp > 0:
    digit = temp % 10          # Get the last digit
    
  
    power_value = 1
    for i in range(count):
        power_value = power_value * digit
        
    total = total + power_value
    temp = temp // 10         

if total == original:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")