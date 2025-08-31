from dataclasses import dataclass, field
from pygame import image


@dataclass
class king:

    """Class that define the king piece in chess."""

    name: str = field(init=False)
    side: str  # Define team side of the piece.
    matrix_pos: tuple  # Define identification in tabletop list.
    vector_moves: list = field(init=False)  # Define how the piece can move.
    moves: list = field(init=False)
    Image: object = field(init=False)  # Define the pygame image object.
    in_check: list = field(init=False)

    def __post_init__(self):

        self.name = "king"
        self.moves = []
        self.in_check = []

        # This section initialize piece image on pygame.
        if self.side == "white":
            self.Image = image.load("pieces_image/white-king.png")
        elif self.side == "black":
            self.Image = image.load("pieces_image/black-king.png")

        # This initialize vector_moves
        self.vector_moves = [(0, 1), (1, 1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

@dataclass
class queen():

    """Class that define the queen piece in chess."""

    name: str = field(init=False)
    side: str  # Define team side of the piece.
    matrix_pos: tuple  # Define identification in tabletop list.
    vector_moves: list = field(init=False)  # Define how the piece can move.
    moves: list = field(init=False)
    Image: object = field(init=False)  # Define the pygame image object.

    def __post_init__(self):

        self.name = "queen"
        self.moves = []

        # This section initialize piece image on pygame.
        if self.side == "white":
            self.Image = image.load("pieces_image/white-queen.png")
        elif self.side == "black":
            self.Image = image.load("pieces_image/black-queen.png")

        # This initialize vector_moves
        self.vector_moves = [(0, 1), (1, 1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]


@dataclass
class knight():

    """Class that define the queen knight in chess."""

    name: str = field(init=False)
    side: str  # Define team side of the piece.
    matrix_pos: tuple  # Define identification in tabletop list.
    vector_moves: list = field(init=False)  # Define how the piece can move.
    moves: list = field(init=False)
    Image: object = field(init=False)  # Define the pygame image object.

    # This section initialize piece image on pygame.
    def __post_init__(self):
        self.name = "knight"
        self.moves = []
        if self.side == "white":
            self.Image = image.load("pieces_image/white-knight.png")
        elif self.side == "black":
            self.Image = image.load("pieces_image/black-knight.png")

        # This initialize vector_moves
        self.vector_moves = [(0, 1), (1, 1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]


@dataclass
class bishop():

    """Class that define the bishop piece in chess."""

    name: str = field(init=False)
    side: str  # Define team side of the piece.
    matrix_pos: tuple  # Define identification in tabletop list.
    vector_moves: list = field(init=False)  # Define how the piece can move.
    moves: list = field(init=False)
    Image: object = field(init=False)  # Define the pygame image object.

    # This section initialize piece image on pygame.
    def __post_init__(self):
        self.name = "bishop"
        self.moves = []
        if self.side == "white":
            self.Image = image.load("pieces_image/white-bishop.png")
        elif self.side == "black":
            self.Image = image.load("pieces_image/black-bishop.png")

        # This initialize vector_moves
        self.vector_moves = [(1, 1), (-1, 1), (-1, -1), (1, -1)]


@dataclass
class rook():

    """Class that define the rook piece in chess."""

    name: str = field(init=False)
    side: str  # Define team side of the piece.
    matrix_pos: tuple  # Define identification in tabletop list.
    vector_moves: list = field(init=False)  # Define how the piece can move.
    moves: list = field(init=False)
    Image: object = field(init=False)  # Define the pygame image object.

    # This section initialize piece image on pygame.
    def __post_init__(self):
        self.name = "rook"
        self.moves = []
        if self.side == "white":
            self.Image = image.load("pieces_image/white-rook.png")
        elif self.side == "black":
            self.Image = image.load("pieces_image/black-rook.png")

        # This initialize vector_moves
        self.vector_moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]


@dataclass
class pawn():

    """Class that define the pawn piece in chess."""

    name: str = field(init=False)
    side: str  # Define team side of the piece.
    matrix_pos: tuple  # Define identification in tabletop list.
    vector_moves: list = field(init=False)  # Define how the piece can move.
    moves: list = field(init=False)
    Image: object = field(init=False)  # Define the pygame image object.

    # This section initialize piece image on pygame.
    def __post_init__(self):
        self.name = "pawn"
        self.moves = []
        if self.side == "white":
            self.Image = image.load("pieces_image/white-pawn.png")
            self.vector_moves = [(-1, 0)]  # This initialize vector_moves for white.
        elif self.side == "black":
            self.Image = image.load("pieces_image/black-pawn.png")
            self.vector_moves = [(1, 0)]  # This initialize vector_moves for black.
