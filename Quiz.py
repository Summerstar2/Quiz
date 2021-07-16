import time
Score=0
print ("Welcome to this Quiz!")
time.sleep(0.8)
print ("This quiz will comprise of 5 general questions and will display you score out of 10 at the end.")
time.sleep(0.8)
Play=str(input("Do you want to start the quiz? (Yes/No) "))
if Play=="No":
    quit()
else:
    print ("The quiz will start in 5..")
    time.sleep(0.7)
    print ("4..")
    time.sleep(0.7)
    print ("3..")
    time.sleep(0.7)
    print ("2..")
    time.sleep(0.7)
    print ("1..")
    time.sleep(0.7)
    print ("Now!")
    time.sleep(0.5)
    print ("Question 1!\nWhat is the capital of India?")
    Ans1=str(input("Enter your answer - "))
    if Ans1=="New Delhi" or "new delhi":
        Score=Score+2
    print ("Question 2!\nHow many continents are there in the world?")
    Ans2=int(input("Enter your answer - "))
    if Ans2==7:
        Score=Score+2
    print ("Question 3!\nWhich is the biggest ocean in the world?")
    Ans3=str(input("Enter your answer - "))
    if Ans3=="Pacific Ocean" or "pacific ocean" or "Pacific ocean":
        Score=Score+2
    print ("Question 4!\nWhich country was Alaska a part of in the 18th century?\nA)USA\nB)Russia\nC)Canada\nD)Denmark")
    Ans4=str(input("Enter your answer - "))
    if Ans4=="Russia":
        Score=Score+2
    print ("Question 5!\nWho is the current president of Russia?")
    Ans5=str(input("Enter you answer - "))
    if Ans5=="Valdmir Putin" or "vladmir putin" or "putin" or "Putin":
        Score=Score+2
    time.sleep(0.5)
    print ("The quiz has now ended and your scores are...")
    time.sleep(1.0)
    print ("You scored", Score, "out of 10!")
