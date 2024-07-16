import random
player1=input("Enter rock, paper or scissors:").lower()
player2=random.choice(["rock","paper","scissors"])
print("Player 2 selected",player2)
if player1=="rock" and player2=="rock":
    print("Tie!")
elif player1=="paper" and player2=="paper":
    print("Tie!")
elif player1=="scissors" and player2=="scissors":
    print("Tie!")
elif player1=="rock" and player2=="scissors":
    print("Player 1 wins!")
elif player1=="paper" and player2=="rock":
    print("Player 1 wins!")
elif player1=="scissors" and player2=="paper":
    print("Player 1 wins!")
elif player1=="scissors" and player2=="rock":
    print("Player 2 wins!")
elif player1=="rock" and player2=="paper":
    print("Player 2 wins!")
elif player1=="paper" and player2=="scissors":
    print("Player 2 wins!")
