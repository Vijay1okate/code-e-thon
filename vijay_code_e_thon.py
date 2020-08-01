n = int(input("enter no of attempts"))                                                             
a = ["1.Aptitude","2.English","3.Math","4.Gk","5.Exit"]                                             
if n==1:
	print(a)
elif n>1:
	print("You are not eligible for test")
else:
	print("Enter correct attempt");



if sub==1:
	print("Thank you for selecting aptitude")
	print(s)
elif sub==2:
	print("Thank you for selecting English")
	print(s)	
elif sub==3:
	print("Thank you for selecting Math")	
	print(s)
elif sub==4:
	print("Thank you for selecting Gk")	
	print(s)
else:
	print("Exit");	

apti_questions = "Aptitude questions"
eng_questions = "English questions"
math_questions = "Math questions"
gk_questions = "Gk questions"

questions=[apti_questions, eng_questions, math_questions, gk_questions]                         

que = {apti_questions:[("2+3=6 is it true", False), ("91 is a prime number?", True)]}           

result = {"correct Answer": 0, "Incorrect Answer": 0}                                           

def get_que_choice():                                                                          
    while True:
        try:
            que_number = int(input("choose the questions you like\n1 for {}\n2:").format(apti_questions))   
        except ValueError:
            print("This is not a number")                                                       
        else:
            if 0>que_number or que_number.len(que):
                print("Please enter correct value")
            else:
                return que_number

