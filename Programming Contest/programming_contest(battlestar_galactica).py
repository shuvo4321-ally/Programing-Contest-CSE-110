# -*- coding: utf-8 -*-


#App 1 
cont=True
while cont==True:
    user_1 = input("Player 1: ").lower()
    user_2 = input("Player 2: ").lower()
    user_3 = input("Player 3: ").lower()
    if user_1 == "paper" and user_2 == "rock" and user_3=="rock":
        print("Player 1 wins")
        cont= False
    elif user_1 == "scissors" and user_2 == "paper" and user_3=="paper":
        print("Player 1 wins")
        cont= False
    elif user_1 == "rock" and user_2=="scissors" and user_3 =="scissors":
        print("Player 1 wins")
        cont= False
    elif user_2 == "paper" and user_1 == "rock" and user_3 == "rock":
        print("Player 2 wins")
        cont= False
    elif user_2 == "scissors" and user_1 == "paper" and user_3 =="paper":
        print("Player 2 wins")
        cont= False
    elif user_2 == "rock" and user_1 == "scissors" and user_3 =="scissors":
        print("Player 2 wins")
        cont= False
    elif user_3 == "paper" and user_1 == "rock" and user_2 == "rock":
        print("Player 3 wins")
        cont= False
    elif user_3 == "scissors" and user_1 == "paper" and user_2 =="paper":
        print("Player 3 wins")
        cont= False
    elif user_3 == "rock" and user_1 == "scissors" and user_2 =="scissors":
        print("Player 3 wins")
        cont= False

#App-2 

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


def check():
    p1 = "x"
    p2 = "o"
    if board[0] == board[1] == board[2] == p1 or board[0] == board[1] == board[2] == p2:
        return True
    elif board[3] == board[4] == board[5] == p1 or board[3] == board[4] == board[5] == p2:
        return True
    elif board[6] == board[7] == board[8] == p1 or board[6] == board[7] == board[8] == p2:
        return True
    elif board[3] == board[0] == board[6] == p1 or board[3] == board[0] == board[6] == p2:
        return True
    elif board[1] == board[4] == board[7] == p1 or board[1] == board[4] == board[7] == p2:
        return True
    elif board[2] == board[5] == board[8] == p1 or board[2] == board[5] == board[8] == p2:
        return True
    elif board[0] == board[4] == board[8] == p1 or board[0] == board[4] == board[8] == p2:
        return True
    elif board[2] == board[4] == board[6] == p1 or board[2] == board[4] == board[6] == p2:
        return True
    else:
        return False


def Inp_ut():
    player1 = int(input("player 1: "))
    if board[player1 - 1] != " " :
        print(" Cannot enter a number that is already taken. Enter again")
        return Inp_ut()
    if (player1-1)<0:
        print("Invalid Input. Enter again")
        return Inp_ut()
    else:
        return (player1)


def Out_ut():
    player2 = int(input("player 2: "))
    if board[player2 - 1] != " ":
        print("Cannot enter a number that is already taken. Enter again")
        return Out_ut()
    if (player2 - 1) < 0:
        print("Invalid Input. Enter again")
        return Out_ut()
    else:
        return (player2)


for i in range(9):
    if i % 2 == 0:
        y = Inp_ut()
        board[y - 1] = "x"
        if check():
            print("player 1 wins!")
            break
        if " " not in board:
            print("It's a tie!")
            break

    else:
        z = Out_ut()
        board[z - 1] = "o"
        if check():
            print("player 2 wins!")
            break
        if " " not in board:
            print("It's a tie!")
            break

#App-2 
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


def Inp_ut():
    player1 = int(input("player 1: "))
    if board[player1 - 1] != " " :
        print(" Cannot enter a number that is already taken. Enter again")
        return Inp_ut()
    if (player1-1)<0:
        print("Invalid Input. Enter again")
        return Inp_ut()
    else:
        return (player1)


def Out_ut():
    player2 = int(input("player 2: "))
    if board[player2 - 1] != " ":
        print(" Cannot enter a number that is already taken. Enter again")
        return Out_ut()
    if (player2 - 1) < 0:
        print("Invalid Input. Enter again")
        return Out_ut()
    else:
        return (player2)


for i in range(9):
    if i % 2 == 0:
        y = Inp_ut()
        board[y - 1] = "x"
        if board[0] == board[1] == board[2] == "x" :
            print("player 1 wins!")
            break
        elif board[3] == board[4] == board[5] == "x" :
            print("player 1 wins!")
            break
        elif board[6] == board[7] == board[8] == "x" :
            print("player 1 wins!")
            break
        elif board[3] == board[0] == board[6] == "x" :
            print("player 1 wins!")
            break
        elif board[1] == board[4] == board[7] == "x" :
            print("player 1 wins!")
            break
        elif board[2] == board[5] == board[8] == "x" :
            print("player 1 wins!")
            break
        elif board[0] == board[4] == board[8] == "x" :
            print("player 1 wins!")
            break
        elif board[2] == board[4] == board[6] == "x" :
            print("player 1 wins!")
            break
        if " " not in board:
            print("It's a tie!")
            break
    else:
        z = Out_ut()
        board[z - 1] = "o"
        if  board[0] == board[1] == board[2] == "o":
            print("player 2 wins!")
            break
        elif  board[3] == board[4] == board[5] == "o":
            print("player 2 wins!")
            break
        elif  board[6] == board[7] == board[8] == "o":
            print("player 2 wins!")
            break
        elif  board[3] == board[0] == board[6] == "o":
            print("player 2 wins!")
            break
        elif  board[1] == board[4] == board[7] == "o":
            print("player 2 wins!")
            break
        elif  board[2] == board[5] == board[8] == "o":
            print("player 2 wins!")
            break
        elif  board[0] == board[4] == board[8] == "o":
            print("player 2 wins!")
            break
        elif board[2] == board[4] == board[6] == "o":
            print("player 2 wins!")
            break
        if " " not in board:
            print("It's a tie!")
            break

#App-2 
a=[]
b=[]
while True:
  p1=int(input("Player 1: "))
  while p1<=0 or p1>9:
    print("Invalid input. Enter again.")
    p1=int(input("Player 1: "))
  while p1 in a or p1 in b:
    print("Cannot enter a number that is already taken. Enter again.")
    p1=int(input("Player 1: "))
    a.append(p1)
  if (1<=p1<=9) and p1 not in a:
    a.append(p1)
  count1=0
  count2=0
  for i in a:
    count1+=1

  if set([1,2,3]).issubset(set(a)) or set([1,4,7]).issubset(set(a)) or set([7,8,9]).issubset(set(a)) or set([3,6,9]).issubset(set(a)) or set([1,5,9]).issubset(set(a))  or set([3,5,7]).issubset(set(a)) or set([4,5,6]).issubset(set(a)) or set([2,5,8]).issubset(set(a)):
    print("Player 1 wins")
    break
  
  elif count1+count2==9:
    print("It's a tie")
    break
  p2=int(input("Player 2: "))
  while p2<=0 or p2>9:
    print("Invalid input. Enter again.")
    p2=int(input("Player 2: "))
  while p2 in a or p2 in b:
    print("Cannot enter a number that is already taken. Enter again.")
    p2=int(input("Player 2: "))
  if (1<=p2<=9) and p2 not in b:
    b.append(p2)
  count1=0
  count2=0
  for i in b:
    count2+=1
  if set([1,2,3]).issubset(set(b)) or set([1,4,7]).issubset(set(b)) or set([7,8,9]).issubset(set(b)) or set([3,6,9]).issubset(set(b)) or set([1,5,9]).issubset(set(b))  or set([3,5,7]).issubset(set(b)) or set([4,5,6]).issubset(set(b)) or set([2,5,8]).issubset(set(b)):
    print("Player 2 wins")
    break
  
  elif count1+count2==9: 
    print("It's a tie")
    break

#App-3 

date=input("Date: ").split("/")
day=int(date[0])
month=int(date[1])
year=int(date[2])

if(day<=0 or month<=0 or year<0):
  print("Invalid Date")
elif (year%4==0):
  if (year%100==0):
    if (year%400==0):
      if (month== 1 or month== 3 or month== 5 or month== 7 or month== 8 or month== 10 or month== 12) and (1<=day<=31) and (0<=year<=2022):
        print("Aladeen Date")
      elif (month==2) and (1<=day<=29):
        print("Aladeen Date")
      elif (month== 4 or month== 6 or month==9 or month==11) and (1<=day<=30) and (0<=year<=2022):
        print("Aladeen Date")
      else:
        print("Invalid date")
    else:
      if (month== 1 or month== 3 or month== 5 or month== 7 or month== 8 or month== 10 or month== 12) and (1<=day<=31) and (0<=year<=2022):
        print("Aladeen Date")
      elif (month==2) and (1<=day<=28):
        print("Aladeen Date")
      elif (month== 4 or month==6 or month==9 or month==11) and (1<=day<=30) and (0<=year<=2022):
        print("Aladeen Date")
      else:
        print("Invalid date")
  else:
    if (month== 1 or month== 3 or month== 5 or month== 7 or month== 8 or month== 10 or month== 12) and (1<=day<=31) and (0<=year<=2022):
      print("Aladeen Date")
    elif (month==2) and (1<=day<=29):
      print("Aladeen Date")
    elif (month== 4 or month==6 or month==9 or month==11) and (1<=day<=30) and (0<=year<=2022):
      print("Aladeen Date")
    else:
      print("Invalid date")
else:
  if (month== 1 or month== 3 or month== 5 or month== 7 or month== 8 or month== 10 or month== 12) and (1<=day<=31) and (0<=year<=2022):
    print("Aladeen Date")
  elif (month==2) and (1<=day<=28):
    print("Aladeen Date")
  elif (month== 4 or month==6 or month==9 or month==11) and (1<=day<=30) and (0<=year<=2022):
    print("Aladeen Date")
  else:
    print("Invalid date")

#App-4 

import re
 
print("Welcome to the Password Validator by Battlestar Galactica!")
user_pass = input("Enter your password: ")
len_pass = len(user_pass)
valid = True
count=0
msg = "Password Invalid! \n"
if not len_pass>=8:
    msg+="Insufficient length. "
    valid = False
if not re.search('[0-9]', user_pass):
    msg+="Digits missing. "
    valid = False
if not re.search('[A-Z]', user_pass):
    msg+="Upper-case missing. "
    valid = False
for i in user_pass:
  if re.search('[a-z]', i): 
    count+=1
if not count>=2:
    msg+= "Insufficient lower-case. "
    valid = False
    
if valid == False:
    print(msg)
  
else:
    print ("Password Valid!")

#App-5 
sides=int(input("No of sides: "))
lst=[]
if (sides==3):
  for i in range(sides):
    l=int(input("Length of sides: "))
    lst.append(l)
  a=lst[0]
  b=lst[1]
  c=lst[2]
  if(a+b>c) and (a+c>b) and (b+c>a):
      print("A triangle can be drawn")
  else:
      print("Invalid input")
elif (sides==4):  
  for i in range(sides):
    l=int(input("Length of sides: "))
    lst.append(l)
  a=lst[0]
  b=lst[1]
  c=lst[2]
  d=lst[3]
  if (b+c+d>a) and (a+c+d>b) and (a+b+d>c) and (a+b+c>d):
      print("A quadrilateral can be drawn")
  else:
      print("Invalid input")
else:
  print("Invalid input")

#App-6 
sides=int(input("No of sides: "))
lst=[]

if sides==3:
  for i in range(sides):
    l=int(input("Angles: "))
    lst.append(l)
  a=lst[0]
  b=lst[1]
  c=lst[2]
  if(a>0) and (b>0) and (c>0):
    if (a+b+c==180):
      if (a==b==c):
        if (a>90) or (b>90) or (c>90):
          print("A equilateral obtuse triangle can be drawn")
        elif (a<90) and (b<90) and (c<90):
          print("A equilateral acute triangle can be drawn")
        elif (a==90) or (b==90) or (b==90):
          print("A equilateral right triangle can be drawn")
      elif (a==b) or (b==c) or (a==c):
        if (a>90) or (b>90) or (c>90):
          print("A isosceles obtuse triangle can be drawn")
        elif (a<90) and (b<90) and (c<90):
          print("A isosceles acute triangle can be drawn")
        elif (a==90) or (b==90) or (b==90):
          print("A isosceles right triangle can be drawn")
      elif(a!=b) and (b!=c) and (a!=c):
        if (a>90) or (b>90) or (c>90):
          print("A scalene obtuse triangle can be drawn")
        elif (a<90) and (b<90) and (c<90):
          print("A scalene acute triangle can be drawn")
        elif (a==90) or (b==90) or (b==90):
          print("A scalene right triangle can be drawn")
      else:
        print("Invalid input")
    else:
      print("Invalid input")
  else:
    print("Angles cannot be zero or negative.")
elif sides==4:
  for i in range(sides):
    l=int(input("Angles: "))
    lst.append(l)
  a=lst[0]
  b=lst[1]
  c=lst[2]
  d=lst[3]
  if(a>0) and (b>0) and (c>0) and (d>0):
    if(a+b+c+d==360):
      if (a==b==c==d==90):
        print("A square or a paralleloghram can")
      elif (a==c) and (b==d):
        print("A rhombus or a rectangle can be drawn")
      else:
        print("A regular quadrilateral can be drawn")
    else:
      print("Invalid input")
  else:
    print("Angles cannot be zero or negative.")
else:
  print("Invalid input")

#App-7 
player1 = []
player2 = []


while True:
    inp = int(input("Player 1: "))
    if sum(player1)+inp <= 25:
        player1.append(inp)

    while player1[-1] == 6 and sum(player1) != 25:
        inp = int(input("Player 1: "))
        player1.append(inp)
        if len(player1) >= 3:
            if player1[-3:] == [6,6,6]:
                player1 = player1[:-3]
                break
    if sum(player1) == 25:
        print("Player 1 wins")
        break

    if sum(player1) == sum(player2):
        player2 = []


    inp = int(input("Player 2: "))
    if sum(player2) + inp <= 25:
        player2.append(inp)

    while player2[-1] == 6  and sum(player2) != 25:
        inp = int(input("Player 2: "))
        player2.append(inp)
        if len(player2) >= 3:
            if player2[-3:] == [6, 6, 6]:
                player2 = player2[:-3]
                break

    if sum(player2) == 25:
        print("Player 2 wins")
        break

    if sum(player1) == sum(player2):
        player1 = []

#App-8 
op=input('''Which Operation you want to perform? (0=Addition, 
1=Subtraction, 2=Multiplication, 3=Division, 4= Floor division, 
5= Exponentiation/ Root Operation, 6= Modulus, 7= Negation, 
8= Compare, 9= State of the number): ''')
if(op=="0" or op=="1" or op=="2" or op=="3" or op=="4" or op=="5" or op=="6" or op=="8"):
  op=int(op)
  inp1=float(input("First Number: "))
  inp2=float(input("Second Number: "))
  if op==0:
    print("Addition:",inp1+inp2)
  elif op==1:
    print("Subtraction:",inp1-inp2)
  elif op==2:
    print("Multiplication:",inp1*inp2)
  elif op==3:
    if inp2==0:
      print("Invalid Input: Division by zero")
    else:
      print("Division:",inp1/inp2)
  elif op==4:
    if inp2==0:
      print("Invalid Input: Division by zero")
    else:
      print("Floor division:",int(inp1//inp2))
  elif op==5:
    if (inp1<0) and (inp2==0.5):
      print("Invalid Input: Root of negative number")
    else:
      print("Exponentiation/Root:",inp1**inp2)
  elif op==6:
    if inp2==0:
      print("Invalid Input: Division by zero")
    else:
      print("Modulas:",int(inp1%inp2))
  elif op==8:
    if inp1>inp2:
      print("First number is greater than second number")
    elif inp1<inp2:
      print("Second number is greater than first number")
    else:
      print("Both numbers are equal")
elif(op=="7" or op=="9"):
  op=int(op)
  inp3=float(input("Number: ")) 
  if op==7:
    print("Negation:",int((-1)*inp3))
  elif op==9:
    if inp3>0:
      print("The number is positive")
    elif inp3<0:
      print("The number is negative")
    else:
      print("The number is zero")
else:
  print("Invalid operation choice")

#app-9 
gcount1=0
gcount2=0
mcount1=0
mcount2=0
for i in range(5):
  if (gcount1==3 and mcount2==3):
    print(f"Team 1 wins by {gcount1}-{gcount2}")
    break
  if (gcount2==3 and mcount1==3):
    print(f"Team 2 wins by {gcount2}-{gcount1}")
    break

  inp1=input("Team 1: ")  
  
  if inp1=="goal":
    gcount1+=1

  if inp1=="miss":
    mcount1+=1

  if (gcount1==3 and mcount2==3):
    print(f"Team 1 wins by {gcount1}-{gcount2}")
    break
  
  if (gcount2==3 and mcount1==3):
    print(f"Team 2 wins by {gcount2}-{gcount1}")
    break
  
  inp2=input("Team 2: ")
  if inp2=="goal":
    gcount2+=1

  if inp2=="miss":
    mcount2+=1
  
  
if (gcount1+mcount1==5) and (gcount2+mcount2==5) and (gcount1>gcount2):
  print(f"Team 1 wins by {gcount1}-{gcount2}")
elif (gcount1+mcount1==5) and (gcount2+mcount2==5) and (gcount2>gcount1):
  print(f"Team 2 wins by {gcount2}-{gcount1}")
elif (gcount1+mcount1==5) and (gcount2+mcount2==5) and (gcount2==gcount1):
  print(f"Draw by {gcount1}-{gcount2}")

#App-10 
turn = 0
end_of_game =False
round=1
player_1_hp=50
player_2_hp=50

player_1 = input("You Choose: ").lower()
player_2 = input("Gary Chooses: ").lower()
while end_of_game == False:

  if player_1_hp <= 0 and player_2_hp<=0:
    end_of_game = True
    print("It's a tie!")
  elif player_1_hp <= 0:
    end_of_game = True
    print(f"{player_2} and Gary wins!")
  elif player_2_hp <= 0:
    end_of_game = True
    print(f"{player_1} and Ash wins!")
  
  else:
    print(f"=== Turn {round} ===")
  if end_of_game == True:
    break

  if (player_1=="charmander" or player_1 == "cyndaquil") and (player_2=="totodile" or player_2=="squirtle"):
      player_1_hp= player_1_hp - 20*2
      player_2_hp = player_2_hp - 20*0.5
      if player_1_hp<0:
        player_1_hp=0
      if player_2_hp<0:
         player_2_hp=0
      print(f"{player_1} has {int(player_1_hp)} hp left")  
      print(f"{player_2} has {int(player_2_hp)} hp left")
      round+=1
  elif (player_1=="charmander" or player_1 == "cyndaquil") and (player_2=="bulbasaur" or player_2=="chikorita"):
        player_1_hp= player_1_hp - 20*0.5
        player_2_hp = player_2_hp - 20*2
        if player_1_hp<0:
          player_1_hp=0
        if player_2_hp<0:
          player_2_hp=0
        print(f"{player_1} has {int(player_1_hp)} hp left")  
        print(f"{player_2} has {int(player_2_hp)} hp left")
        round+=1    
  elif (player_1=="squirtle" or player_1 == "totodile") and (player_2=="charmander" or player_2=="cyndaquil"):
        player_1_hp= player_1_hp - 20*0.5
        player_2_hp = player_2_hp - 20*2
        if player_1_hp<0:
          player_1_hp=0
        if player_2_hp<0:
          player_2_hp=0
        print(f"{player_1} has {int(player_1_hp)} hp left")  
        print(f"{player_2} has {int(player_2_hp)} hp left")
        round+=1  
  elif (player_1=="squirtle" or player_1 == "totodile") and (player_2=="chikorita" or player_2=="bulbasaur"):
          player_1_hp= player_1_hp - 20*2
          player_2_hp = player_2_hp - 20*0.5
          if player_1_hp<0:
            player_1_hp=0
          if player_2_hp<0:
            player_2_hp=0
          print(f"{player_1} has {int(player_1_hp)} hp left")  
          print(f"{player_2} has {int(player_2_hp)} hp left")
          round+=1  
  elif (player_1=="bulbasaur" or player_1 == "chikorita") and (player_2=="charmander" or player_2=="cyndaquil"):
          player_1_hp= player_1_hp - 20*2
          player_2_hp = player_2_hp - 20*0.5
          if player_1_hp<0:
            player_1_hp=0
          if player_2_hp<0:
            player_2_hp=0
          print(f"{player_1} has {int(player_1_hp)} hp left")  
          print(f"{player_2} has {int(player_2_hp)} hp left")
          round+=1    
  elif (player_1=="bulbasaur" or player_1 == "chikorita") and (player_2=="squirtle" or player_2=="totodile"):
          player_1_hp= player_1_hp - 20*0.5
          player_2_hp = player_2_hp - 20*2
          if player_1_hp<0:
            player_1_hp=0
          if player_2_hp<0:
            player_2_hp=0
          print(f"{player_1} has {int(player_1_hp)} hp left")  
          print(f"{player_2} has {int(player_2_hp)} hp left")
          round+=1 
  else:
          player_1_hp= player_1_hp - 20
          player_2_hp = player_2_hp - 20
          if player_1_hp<0:
              player_1_hp=0
          if player_2_hp<0:
              player_2_hp=0
          print(f"{player_1} has {int(player_1_hp)} hp left")  
          print(f"{player_2} has {int(player_2_hp)} hp left")
          round+=1