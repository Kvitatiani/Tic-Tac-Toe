# Tic Tac Toe

def game():
    game_is_on = True

    # Drawing a board
    board = "|1|2|3|\n|4|5|6|\n|7|8|9|"

    # Ask player1 to choose their sign, player2 chooses the opposite sign automatically
    player1 = input(
        "Welcome to tic-tac-toe; Player 1 please choose: 'X' or 'O': ").upper()
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    while game_is_on:

        # Ask player1 for their choice of spot
        player1_choice = input(
            "Player1, please choose the spot from 1 to 9 including, where you would like to place the sign: ")

        # Check if the player1 spot is not taken
        if player1_choice == "stop":
            game_is_on = False
            break
        else:
            while player1_choice not in board:
                player1_choice = input(
                    "Player1, that spot is taken, please choose a different spot: ")
            else:
                board = board.replace(player1_choice, player1)
                print(board)

        # Check for the winner
        if (board[1] == board[3] == board[5]):
            print(f"Game over, {board[1]} is the winner!")
            break
        elif (board[9] == board[11] == board[13]):
            print(f"Game over, {board[9]} is the winner!")
            break
        elif (board[17] == board[19] == board[21]):
            print(f"Game over, {board[17]} is the winner!")
            break
        elif (board[1] == board[9] == board[17]):
            print(f"Game over, {board[1]} is the winner!")
            break
        elif (board[3] == board[11] == board[19]):
            print(f"Game over, {board[3]} is the winner!")
            break
        elif (board[5] == board[13] == board[21]):
            print(f"Game over, {board[5]} is the winner!")
            break
        elif (board[1] == board[11] == board[21]):
            print(f"Game over, {board[1]} is the winner!")
            break
        elif (board[5] == board[11] == board[17]):
            print(f"Game over, {board[5]} is the winner!")
            break

        player2_choice = input(
            "Player2, please choose the spot from 1 to 9 including, where you would like to place the sign: ")

        # Check if the player2 spot is not taken
        if player2_choice == "stop":
            game_is_on = False
            break
        else:
            while player2_choice not in board:
                player2_choice = input(
                    "Player2, that spot is taken please choose a different spot: ")
            else:
                board = board.replace(player2_choice, player2)
                print(board)

        # Check for the winner
        if (board[1] == board[3] == board[5]):
            print(f"Game over, {board[1]} is the winner!")
            break
        elif (board[9] == board[11] == board[13]):
            print(f"Game over, {board[9]} is the winner!")
            break
        elif (board[17] == board[19] == board[21]):
            print(f"Game over, {board[17]} is the winner!")
            break
        elif (board[1] == board[9] == board[17]):
            print(f"Game over, {board[1]} is the winner!")
            break
        elif (board[3] == board[11] == board[19]):
            print(f"Game over, {board[3]} is the winner!")
            break
        elif (board[5] == board[13] == board[21]):
            print(f"Game over, {board[5]} is the winner!")
            break
        elif (board[1] == board[11] == board[21]):
            print(f"Game over, {board[1]} is the winner!")
            break
        elif (board[5] == board[11] == board[17]):
            print(f"Game over, {board[5]} is the winner!")
            break


game()
