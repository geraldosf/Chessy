from objects.chess_pos import chess_pos


def mount_tabletop():

    """Function to start all squares of the tabletop 8x8"""

    tabletop = [[], [], [], [], [], [], [], []]

    for i in range(8):
        for j in range(8):
            height = 115  # Height of the square.
            width = 120  # Width of the square.
            padding_x = 20  # Left padding.
            padding_y = 45  # Top padding.
            pos = (padding_x + width * j, padding_y + height * i)  # Calculate the right position of each square.
            label = chr(97 + j) + str(8 - i)  # Calculate the label of the square.
            matrix_pos = (i, j)  # Define position in tabletop list.
            tabletop[i].append(chess_pos(label, matrix_pos, pos, width, height))  # Add square to tabletop.

    return tabletop


def refresh_moves(tabletop: list) -> None:
    
    for i in range(8):
        for j in range(8):
            square = tabletop[i][j]
            if square.piece is not None:
                square.piece.moves = calculate_moves(square.piece, tabletop)


def calculate_moves(piece: object, tabletop: list, capture: bool = False):

    """Function that calculate legal moves."""

    pos = piece.matrix_pos  # Define starting position in tabletop list
    vector = piece.vector_moves  # Define in which directions the piece can move.

    moves = []  # Initialize legal moves.

    king_pos = find_king_pos(tabletop, piece.side)

    threat_list = get_threat_list(tabletop, piece.side)


    for i in range(len(vector)):
        j = 0

        while True:
            if piece.__class__.__name__ == "knight": 

                if vector[i][0] == vector[i][1]:
                    if vector[i][0] > 1:
                        y_movement = 2 * vector[i][0]
                        x_movement = 1
                    else:
                        y_movement = 2 * vector[i][0]
                        x_movement = -1
                elif abs(vector[i][0]) == abs(vector[i][1]):
                    y_movement = -1
                    x_movement = 2 * vector[i][1]      
                else:
                    if vector[i][0] == 0:
                        y_movement = 1
                    else:
                        y_movement = 2 * vector[i][0]

                    if vector[i][1] == 0:
                        x_movement = + 1
                    else:
                        x_movement = 2 * vector[i][1]
                

                possible_pos = (pos[0] + y_movement, pos[1] + x_movement)
            else:
                possible_pos = (pos[0] + (j + 1) * vector[i][0], pos[1] + (j + 1) * vector[i][1])

            # This section check if the position isn't out of the tabletop.
            if possible_pos[0] > 7 or possible_pos[1] > 7:
                break
            elif possible_pos[0] < 0 or possible_pos[1] < 0:
                break

            possible_square = tabletop[possible_pos[0]][possible_pos[1]]
            
            # Check if there is some piece in the position
            if possible_square.piece != None:
                if piece.side == possible_square.piece.side:
                    break
                if possible_square.piece.name == "king":
                    if possible_square.piece.side != piece.side:
                        possible_square.piece.in_check.append(piece)
                        print("Check")
                    break

            moves.append(possible_pos)  # Add to a list of legal moves.
            j += 1

            if possible_square.piece != None:
                break

            # Pawn is a special piece.
            if piece.name == "pawn":
                if possible_pos[0] == 5 or possible_pos[0] == 2:
                    continue
                else:
                    break
            elif piece.name == "knight" or piece.name == "king":
                break

    return moves


def move_piece(square: object, position: object, tabletop: object):

    """Function to move a piece along tabletop"""

    square.piece.matrix_pos = position.matrix_pos
    position.piece = square.piece
    square.piece = None
    refresh_moves(tabletop)


def find_king_pos(tabletop: list, side: str):

    for i in range(8):
        for j in range(8):
            square = tabletop[i][j]

            if square.piece != None and square.piece.name == "king":
                if square.piece.side == side:
                    return square.piece
                

def get_threat_list(tabletop: list, ops_side: str):

    threat_list = []

    for i in range(8):
        for j in range(8):
            square = tabletop[i][j]

            if square.piece != None and square.piece.side != ops_side:
                for vector in square.piece.moves:
                    threat_list.append(vector)

    return threat_list
                