#!/usr/bin/python3

def print_board(board):
    """Affiche le plateau de jeu."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Vérifie s'il y a un gagnant."""
    # Vérification des lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérification des colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """Joue une partie de Tic Tac Toe entre deux joueurs."""
    board = [[" "]*3 for _ in range(3)]  # Créer un plateau de 3x3 vide
    player = "X"  # Le premier joueur est "X"
    
    while not check_winner(board):  # Tant qu'il n'y a pas de gagnant
        print_board(board)
        
        # Demander à l'utilisateur de saisir une ligne et une colonne
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                
                # Vérifier si les indices sont valides et si la case est vide
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if board[row][col] == " ":
                        break  # Quitter la boucle si la case est valide
                    else:
                        print("That spot is already taken! Try again.")
                else:
                    print("Invalid input. Please enter a row and column between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        # Placer le jeton du joueur dans la case
        board[row][col] = player

        # Alterner les joueurs
        player = "O" if player == "X" else "X"
    
    print_board(board)
    # Le dernier joueur a fait le coup gagnant, donc afficher celui-là
    winner = "O" if player == "X" else "X"
    print(f"Player {winner} wins!")

tic_tac_toe()
