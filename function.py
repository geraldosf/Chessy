from objects.chess_pos import chess_pos


def mount_tabletop():

    """Function to start all squares of the tabletop 8x8"""

    tabletop = [[], [], [], [], [], [], [], []]

    for i in range(8):
        for j in range(8):
            height = 115  # Height of the square.
            width = 120  # Width of the square.
            padding_x = 20  # Left padding.
            padding_y = 25  # Top padding.
            pos = (padding_x + width * j, padding_y + height * i)  # Calculate the right position of each square.
            label = chr(97 + j) + str(8 - i)  # Calculate the label of the square.
            matrix_pos = (i, j)  # Define position in tabletop list.
            tabletop[i].append(chess_pos(label, matrix_pos, pos, width, height))  # Add square to tabletop.

    return tabletop


def calculate_moves(piece: object, tabletop: list):

    """Function that calculate legal moves."""

    pos = piece.matrix_pos  # Define starting position in tabletop list
    vector = piece.vector_moves  # Define in which directions the piece can move.

    moves = []  # Initialize legal moves.

    for i in range(len(vector)):
        j = 0

        while True:
            possible_pos = (pos[0] + (j + 1) * vector[i][0], pos[1] + (j + 1) * vector[i][1])

            # This section check if the position isn't out of the tabletop.
            if possible_pos[0] > 7 or possible_pos[1] > 7:
                break
            elif possible_pos[0] < 0 or possible_pos[1] < 0:
                break

            # Check if there is some piece in the position
            if tabletop[possible_pos[0]][possible_pos[1]].piece is not None:
                break

            moves.append(possible_pos)  # Add to a list of legal moves.
            j += 1

            # Pawn is a special piece.
            if piece.__class__.__name__ == "pawn":
                break

    return moves


def move_piece(square: object, position: object):

    """Function to move a piece along tabletop"""

    square.piece.matrix_pos = position.matrix_pos
    position.piece = square.piece
    square.piece = None
