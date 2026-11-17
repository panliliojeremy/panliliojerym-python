
print("="*55)
print("Jee3 Python Tutorial")
print("="*55)
print("Prelim")
print("Midterm")
print("Finals")
print("="*55)

techoi = input("Select a term: ")

if techoi == "Prelim":

    while True:
        print("="*55)
        print("PRELIM LESSONS")
        print("="*55)
        print("L1 - Introduction To Programming")
        print("L2 - Python Basic Syntax")
        print("L3 - Arithmetic Operators And Expressions")
        print("L4 - Basic Input and Output in Python")
        print("0 - Back to Term Selection")
        print("="*55)

        prechoi = input("Select A Lesson: ")

        if prechoi == "L1":
           print("="*55)
           print("Introduction To Programming")
           print("So What is Programming?")
           print("Program Language - was a language that used to make code and to run a program")

           print("Example of Language Program:")
           print("Python")
           print("Java")
           print("JavaScript")
           print("C/C+")
           print("What is Python?")
           print("Python is a programming language that widely used for coders or programmer")
           print("="*55)

        elif prechoi == "L2":
            print("="*55)
            print("What is Python Syntax")
            print("Python Syntax is the one that tells us the correct way to put our code")
            print("What are those")
            print("1. Printing Output")
            print("- It was used to show or display our output")
            print("Printing Statement")
            print("print()")
            print("2. Printing Text")
            print("- You can also use it with text or number or a variable")
            print("Example:")
            print('print("HELLO WORLD")')
            print("3. Printing Numbers")
            print("print(101)")
            print("4. Python Comments")
            print("- Python comments are ignored by using a #")
            print("5. Variables, Constant And Data Types")
            print("What is Variables?")
            print("- Variables are like our storage to keep a text or number")
            print("Example: name = 'John'")
            print("age = 19")
            print("Rules:")
            print("- Variables should not start with a number")
            print("="*55)

        elif prechoi == "L3":
            print("="*55)
            print("What is Arithmetic Operators?")
            print("- Arithmetic operators are symbols used for mathematical calculations")
            print("Such as:")
            print("Addition = 1 + 1")
            print("Subtraction = 1 - 1")
            print("Multiplication = 1 * 1")
            print("Division = 1 / 1")
            print("Floor Division = 1 // 1")
            print("Modulus = 1 % 1")
            print("Exponentiation = 1 ** 1")
            print("Example of Expression:")
            print("a = 3")
            print("b = 7")
            print("a + b = 10")
            print("="*55)

        elif prechoi == "L4":
            print("="*55)
            print("What is Basic Input and Output?")
            print("- It is used to get information from the user and display results")
            print("1. Formatting Input")
            print("Example:")
            print('name = input("Enter Your name: ")')
            print('age = int(input("Enter Your age: "))')
            print("2. Float Input")
            print("Example:")
            print('grade = float(input("Enter Your Grade: "))')
            print("3. Boolean Input")
            print("Example:")
            print('answer = input("Are you okay? (yes or no): ")')
            print("="*55)
            
       
        elif prechoi == "0":
            print("Going back to Term Selection...")
            break
            
        else:
            print("="*55)
            

elif techoi == "Midterm":
   while True:
       print("="*55)
       print("Midterm Lesson")
       print("="*55)
       print("L1 - Conditional Statements In Python")
       print("L2 - Logical Operator")
       print("0 - Back to Term Selection")
       print("="*55)
      
       mechoi = input("Select A Lesson:")
     
       if mechoi == "L1":
           print("What is Conditional Statement")
           print("- it allows the program to make a decision (true/false)")
           print("What is Relational Operators")
           print("-it's used to allow the program to compare the number if its true or false")
           print("The If Statement")
           print("- it execute the a block of code")
           print("The if-else statement")
           print("-it provide a other conditions if the if statement are false")
           print("What is Nested Condition?")
           print("-nested condition is a condition inside of the other condition")
       elif mechoi == "L2":
           print("What are Logical Operators?")
           print("and- this operators will only be true if both conditions are true")
           print("or - this operator will only be true if one the condition are true")
           print("not - it reverses the result of the condition you have")
       elif mechoi == "0":
           print("Going back to Term Selection..... ")
           break
       else:
           print("="*55)
           
elif techoi == "Finals":
         while True:
            print("="*55)
            print("Finals Lesson")
            print("="*55)
            print("L1 -Iteration And Loops")
            print("0 - Back to Term Selection")
            print("="*55)
            
            fichoi = input("Select A Leson:")
            if fichoi == "L1":
                print("What is Iteration?")
                print("- iteration is where a repeating process at program happens")
                print("Types of Loop")
                print("Without Loop")
                print("print('Hello')")
                print("print('Hello')")
                print("print('Hello')")
                print("For Loop")
                print("for number in range(10)")
                print("Hello")
                print("While Loop")
                print("count = 2")
                print("while count <= 10:")
                print("Harrrr")
                print("+= 2")
            
                
            elif fichoi == "0":
                print("Going back to Term Selection....")
                break
            else:
                print("="*55)                               
      
else:
      ("Thank You")    
      
      
      
# sec9


te2choi = input("Go to Main Menu:?")

if te2choi == "Yes":
     print("="*55)
     print("Jee3 Python Tutorial")
     print("="*55)
     print("Prelim")
     print("Midterm")
     print("Finals")
     print("="*55)

     te1choi = input("Select a term: ")

     if te1choi == "Prelim":
        while True:
           print("="*55)
           print("PRELIM LESSONS")
           print("="*55)
           print("L1 - Introduction To Programming")
           print("L2 - Python Basic Syntax")
           print("L3 - Arithmetic Operators And Expressions")
           print("L4 - Basic Input and Output in Python")
           print("0 - Exit")
           print("="*55)

           prechoi = input("Select A Lesson: ")

           if prechoi == "L1":   
            print("="*55)
            print("Introduction To Programming")
            print("So What is Programming?")
            print("Program Language - was a language that used to make code and to run a program")

            print("Example of Language Program:")
            print("Python")
            print("Java")
            print("JavaScript")
            print("C/C+")
            print("What is Python?")
            print("Python is a programming language that widely used for coders or programmer")
            print("="*55)
           

           elif prechoi == "L2":           
            print("="*55)
            print("What is Python Syntax")
            print("Python Syntax is the one that tells us the correct way to put our code")
            print("What are those")
            print("1. Printing Output")
            print("- It was used to show or display our output")
            print("Printing Statement")
            print("print()")
            print("2. Printing Text")
            print("- You can also use it with text or number or a variable")
            print("Example:")
            print('print("HELLO WORLD")')
            print("3. Printing Numbers")
            print("print(101)")
            print("4. Python Comments")
            print("- Python comments are ignored by using a #")
            print("5. Variables, Constant And Data Types")
            print("What is Variables?")
            print("- Variables are like our storage to keep a text or number")
            print("Example: name = 'John'")
            print("age = 19")
            print("Rules:")
            print("- Variables should not start with a number")
            print("="*55)

           elif prechoi == "L3":
            print("="*55)
            print("What is Arithmetic Operators?")
            print("- Arithmetic operators are symbols used for mathematical calculations")
            print("Such as:")
            print("Addition = 1 + 1")
            print("Subtraction = 1 - 1")
            print("Multiplication = 1 * 1")
            print("Division = 1 / 1")
            print("Floor Division = 1 // 1")
            print("Modulus = 1 % 1")
            print("Exponentiation = 1 ** 1")
            print("Example of Expression:")
            print("a = 3")
            print("b = 7")
            print("a + b = 10")
            print("="*55)

           elif prechoi == "L4":
            print("="*55)
            print("What is Basic Input and Output?")
            print("- It is used to get information from the user and display results")
            print("1. Formatting Input")
            print("Example:")
            print('name = input("Enter Your name: ")')
            print('age = int(input("Enter Your age: "))')
            print("2. Float Input")
            print("Example:")
            print('grade = float(input("Enter Your Grade: "))')
            print("3. Boolean Input")
            print("Example:")
            print('answer = input("Are you okay? (yes or no): ")')
            print("="*55)
            
       
           elif prechoi == "0":
            print("Exit")
            break
            
        else:
            print("="*55)
   
           
     elif te1choi == "Midterm":
        while True:
            print("="*55)
            print("Midterm Lesson")
            print("="*55)
            print("L1 - Conditional Statements In Python")
            print("L2 - Logical Operator")
            print("0 - Exit")
            print("="*55)
      
            mechoi = input("Select A Lesson:")
     
            if mechoi == "L1":
             print("What is Conditional Statement")
             print("- it allows the program to make a decision (true/false)")
             print("What is Relational Operators")
             print("-it's used to allow the program to compare the number if its true or false")
             print("The If Statement")
             print("- it execute the a block of code")
             print("The if-else statement")
             print("-it provide a other conditions if the if statement are false")
             print("What is Nested Condition?")
             print("-nested condition is a condition inside of the other condition")
            elif mechoi == "L2":
             print("What are Logical Operators?")
             print("and- this operators will only be true if both conditions are true")
             print("or - this operator will only be true if one the condition are true")
             print("not - it reverses the result of the condition you have")
            elif mechoi == "0":
             print("Exit")
             break
            else:
             print("="*55)
           
     elif te1choi == "Finals":
        while True:
            print("="*55)
            print("Finals Lesson")
            print("="*55)
            print("L1 -Iteration And Loops")
            print("0 - Exit")
            print("="*55)
            
            fichoi = input("Select A Leson:")
            if fichoi == "L1":
                print("What is Iteration?")
                print("- iteration is where a repeating process at program happens")
                print("Types of Loop")
                print("Without Loop")
                print("print('Hello')")
                print("print('Hello')")
                print("print('Hello')")
                print("For Loop")
                print("for number in range(10)")
                print("Hello")
                print("While Loop")
                print("count = 2")
                print("while count <= 10:")
                print("Harrrr")
                print("+= 2")
            
                
            elif fichoi == "0":
                print("Exit")
                break
            else:
                print("="*55)                
     
else:
    print("Thank you")
    print("Make sure to take a Quiz")
    
  
 # Quiz
print("="*55)
print("Quiztime")
print("="*55) 
    
score = 0
quichoi = input("Are you ready to take a quiz?")

if quichoi == "Yes":
    print("1.What is the use of Python syntax")
    print("A) To tell us the right number")
    print("B) To tell us the correct way to put the code")
    print("C) To remind the limit letter")
    ans = input("Your Answer:").upper()

    if ans == "B":
     print("Correct Answer")
     score += 1
     
    else:
     print("Wrong Answer")
     print("The correct Answer is C")
     
     print("2. What is the correct way to print number")
     print("A). print(101)")
     print("B). print[101]")
     print("C).print{101} ")
     ans = input("Your Answer:")
  
     if ans == "A":
      print("Correct Answer")
      score += 1
     else:
      print("Wrong Answer")
      print("The correct Answer is C")
      
   
     print("3. Why do we use python comments")
     print("A) To delete the code")
     print("B) To make a design")
     print("C) To give a name to program to remember ")
     ans = input("Your Answer:")
  
     if ans == "C":
      print("Correct Answer")
      score += 1
     else:
      print("Wrong Answer")
      print("The Correft Answer is A")
      
      print("4. What is the use of Programming")
      print("A) To play games")
      print("B) To Watch Videos")
      print("C) To run code you created")
      ans = input("Your Answer:").upper()

      if ans == "C":
       print("Correct Answer")
       score += 1
     
      else:
       print("Wrong Answer")
       print("The correct Answer is C")
  
      print("5. What is the language we are learning")
      print("A) Python Language")
      print("B) Java")
      print("C) Ruby")
      ans = input("Your Answer:")
  
      if ans == "A":
       print("Correct Answer")
       score += 1
      else:
       print("Wrong Answer")
       print("The correct Answer is C")
       
   
      print("6. Why we need to learn Python")
      print("A) Because it's easy and simple")
      print("B) To read a book")
      print("C) Because it's complicated")
      ans = input("Your Answer:")
  
      if ans == "A":
       print("Correct Answer")
       score += 1
      else:
       print("Wrong Answer")
       print("The Correft Answer is A")

    print("7.What is the condition of and")
    print("A) True and False")
    print("B) True and True")
    print("C) False and False")
    ans = input("Your Answer:").upper()

    if ans == "B":
     print("Correct Answer")
     score += 1
     
    else:
     print("Wrong Answer")
     print("The correct Answer is C")
  
    print("8. What is the operators of floor division")
    print("A) 1*1")
    print("B) 1%1")
    print("C) 1//1")
    ans = input("Your Answer:")
  
    if ans == "C":
     print("Correct Answer")
     score += 1
    else:
     print("Wrong Answer")
     print("The correct Answer is C")
      
   
    print("9. What is conditional statements ")
    print("A) To allow you to make decision")
    print("B) To allow the program make decision")
    print("C) To tell if it's true")
    ans = input("Your Answer:")
  
    if ans == "B":
     print("Correct Answer")
     score += 1
    else:
     print("Wrong Answer")
     print("The Correft Answer is A")
     
    print("10.What is the use looping")
    print("A) To print faster if you want to print multiple ")
    print("B) To make it steady")
    print("C) To run code faster")
    ans = input("Your Answer:").upper()

    if ans == "A":
     print("Correct Answer")
     score += 1
     
    else:
     print("Wrong Answer")
     print("The correct Answer is C")
     
print("="*55)
print("Quiz Result")
print("="*55)
print("Your Score:", score,  "/10")
print("Thank youuuu")
  


      
      
      
      
      

       
       
       
       
     
       
 


