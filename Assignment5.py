print("ChatBot for  Question and Answering ") 
print("=====================================") 
print(" You may ask any one of these questions") 
print("Hi") 
print("How are you?") 
print("Are you working?") 
print("What is your name?") 
print("what did you do yesterday?")
print("How is the weather today")
print("What is your favourite color")
print("What is the current price of apache 1604v")
print("Quit") 
while True: 
 question = input("Enter one question from above list:") 
 question = question.lower() 
 if question in ['hi']: 
     print("Hello") 
 elif question in ['how are you?','how do you do?']: 
     print("I am fine") 
 elif question in ['are you working?','are you doing any job?']: 
     print("Yes. I'am working in ADYSOE,Lohegaon") 
 elif question in ['what is your name?']: 
     print("My name is ChatBot") 
     name=input("Enter your name?")
     print("Nice name and Nice meeting you",name) 
 elif question in ['what did you do yesterday?']: 
     print("Yesterday I am very busy in Writing Assignments") 
 elif question in ['how is the weather today']: 
     print("Its Sunny outside") 
 elif question in ['what is your favourite color']: 
     print("Blue") 
 elif question in ['What is the current price of apache 1604v']: 
     print("1,60,000") 
 elif question in ['quit']: 
         break 
 else: 
     print("I don't understand what you said")