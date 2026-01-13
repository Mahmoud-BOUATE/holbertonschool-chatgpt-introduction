#!/usr/bin/python3

def print_board(board):
    """Affiche le plateau de jeu."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # Plus lisible pour 3x3

def check_winner(board):
    """Vérifie si un joueur a gagné."""
    # Vérifier les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérifier les colonnes
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifier les diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def board_full(board):
    """Vérifie si le plateau est plein (match nul)."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Fonction principale du jeu Tic Tac Toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        # Saisie sécurisée
        try:
            row = int(input(f"Enter row (0, 1, 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, 2) for player {player}: "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Valeur invalide ! Les coordonnées doivent être 0, 1 ou 2.")
                continue
        except ValueError:
            print("Entrée invalide ! Veuillez entrer un nombre entier.")
            continue

        if board[row][col] != " ":
            print("Cette case est déjà prise ! Réessayez.")
            continue

        # Placer le coup
        board[row][col] = player

        # Vérifier si le joueur a gagné
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Vérifier match nul
        if board_full(board):
            print_board(board)
            print("Match nul !")
            break

        # Changer de joueur
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
