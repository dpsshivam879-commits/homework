print("AT LEAST 75% ATTENDANCE IS REQUIRED TO BE ELIGIBLE FOR THE EXAM")
name=input("enter your name:")
print("lets calculate your attendance",name)
total=180 
attended=int(input("enter no.of days present"))
percentage = (attended / total) * 100
if percentage >= 75:
    print("Congratulations!, you are eligible for the exam")
else:
    print("Please submit all your leave documents and we will get back to you shortly")