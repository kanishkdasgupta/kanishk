import random


try:
    # Function to print the Tic-Tac-Toe board
    def print_board(board):
        for row in board:
            print("    |  ".join(row))
            print("--" * 9)

    # if the player wins na then this will happen
    def check_win(board, player):
        for row in board:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(row[col] == player for row in board):
                return True

        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return True

        return False

    #if board full
    def is_board_full(board):
        return all(cell != " " for row in board for cell in row)

    # Comps turn
    def computer_move(board):
        print("COMPUTER'S TURN")
        available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
        if available_moves:
            return random.choice(available_moves)
        return None

    # MAIN LOOP (KANISHKS TURN)

    def play_game():
        board = [[" " for _ in range(3)] for _ in range(3)]
        player = "X"
        computer = "O"
        
        while True:
            print_board(board)
            
            if player == "X":
                print("You are X")
                row, col = map(int, input("Enter your move:\n first value should be which row \n second value should be which column \n (To enter 1st row, you write '0', 2nd row, write '1', 3rd row, write '2' and same for columns \n Example: to enter the top left box, you write 0 0): ").split())
            else:
                row, col = computer_move(board)
            
            if board[row][col] == " ":
                board[row][col] = player
                if check_win(board, player):
                    print_board(board)
                    print(f"{player} wins! Congratulations!")
                    break
                if is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                player = "O" if player == "X" else "X"
            else:
                print("Invalid move. Try again.")
            

    if __name__ == "__main__":
        while True:
            try:
                play_game()
                break  # If the game finishes successfully, break out of the loop
            except Exception as e:
                print("An error occurred:", e)
                print("Restarting the game...")
except:
    print("oops")

