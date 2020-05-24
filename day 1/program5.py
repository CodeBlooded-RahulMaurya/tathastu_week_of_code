print("Enter runs by players in 60 balls : ")
runP1 = int(input("By Player 1 in 60 balls: "))
runP2 = int(input("By player 2 in 60 balls: "))
runP3 = int(input("By player 3 in 60 balls: "))
strikerate1 = runP1 * 100 / 60
strikerate2 = runP2 * 100 / 60
strikerate3 = runP3 * 100 / 60
print("Strike rate of players are ")
print("Player 1  : ", strikerate1)
print("Player 2  : ", strikerate2)
print("Player 3  : ", strikerate3)
print("Runs scored by players  if they played 60 more balls are : ")
print("Player 1  : ",runP1 * 2 )
print("Player 2  : ", runP2 * 2)
print("Player 3  : ", runP3 * 2)
print("Maximum number of 6's players could hit ")
print("Player 1  : ", runP1 // 6)
print("Player 2  : ", runP2 // 6)
print("Player 3  : ", runP3 // 6)