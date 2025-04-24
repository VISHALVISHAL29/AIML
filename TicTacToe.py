B = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]


def Board(B):
    print(B[0], "|", B[1], "|", B[2])
    print(B[3], "|", B[4], "|", B[5])
    print(B[6], "|", B[7], "|", B[8])


def Player():
    print("Player 1 Choose your Varibale : ")
    player1 = input("Choose Your Variable : ")
    print("Player 2 Choose your Variable")
    player2 = input("Choose Your Variable : ")
    while True:
        if player1 == player2:
            print("Both players can't have the same variable. Choose again.")
            return Player()
        elif player1 not in ["X", "O"] or player2 not in ["X", "O"]:
            print("Please choose from the given variables: X or O.")
            return Player()
        else:
            return player1, player2


def Input(B, player1, player2):
    turn = player1
    for i in range(len(B)):
        print("\n"+turn+"'"+"s Turn")
        num = int(input("Enter A num :"))

        while num < 0 or num > 9  or B[num] != "_":
         print("Invalid Input Re-enter Num \t")
         num = int(input("Enter A num :"))

        B[num] = turn
        Board(B)
        if decision(B, turn):
            print(turn + " is the winner!")
            return
        turn = player2 if turn == player1 else player1
    print("It's a draw.")

def decision(B,turn):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    
    for pos in win_positions:

        if(B[pos[0]]==B[pos[1]]==B[pos[2]]==turn):
          return True

    return False

        



Board(B)
player1, player2 = Player()
Input(B, player1, player2)
