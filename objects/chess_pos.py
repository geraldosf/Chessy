from dataclasses import field, dataclass
from objects.pieces import pawn, queen, king, rook, knight, bishop
from pygame import Rect


@dataclass
class chess_pos:

    """This is the class that represent the square in tabletop."""

    label: str  # Define identification of the square in chess.
    matrix_pos: tuple  # Define identification in tabletop list.
    pos: tuple  # Define identification in pygame position tuple.
    pos_center: tuple = field(init=False)  # Define the center of the square in pygame position.
    image_pos: tuple = field(init=False)  # Define the position to create image
    width: int  # Define the widht of the square.
    height: int  # Define the height of the square.
    rect: object = field(init=False)  # Define object retangule for pygame.
    piece: object = None  # Define which piece is on this position.

    def __post_init__(self) -> None:

        self.image_pos = (self.pos[0] - 6, self.pos[1] - 8)  # Adjust the image to the square.
        self.rect = Rect(self.pos[0], self.pos[1], self.width, self.height)  # Initialize pygame object retangule.
        self.pos_center = (self.pos[0] + self.width / 2, self.pos[1] + self.height / 2)  # Calculate the center position.

        self.create_vanilla()

    def create_vanilla(self) -> None:

        """Method create pieces in vanilla chess."""

        # This section create the piece on the right squares.
        if self.label == "a1" or self.label == "h1":
            self.piece = rook("white", self.matrix_pos)
        elif self.label == "b1" or self.label == "g1":
            self.piece = knight("white", self.matrix_pos)
        elif self.label == "c1" or self.label == "f1":
            self.piece = bishop("white", self.matrix_pos)
        elif self.label == "d1":
            self.piece = queen("white", self.matrix_pos)
        elif self.label == "e1":
            self.piece = king("white", self.matrix_pos)
        else:
            for i in range(8):
                if self.label == chr(ord(self.label[0]) + i) + "2":
                    self.piece = pawn("white", self.matrix_pos)

        if self.label == "a8" or self.label == "h8":
            self.piece = rook("black", self.matrix_pos)
        elif self.label == "b8" or self.label == "g8":
            self.piece = knight("black", self.matrix_pos)
        elif self.label == "c8" or self.label == "f8":
            self.piece = bishop("black", self.matrix_pos)
        elif self.label == "d8":
            self.piece = queen("black", self.matrix_pos)
        elif self.label == "e8":
            self.piece = king("black", self.matrix_pos)
        else:
            for i in range(8):
                if self.label == chr(ord(self.label[0]) + i) + "7":
                    self.piece = pawn("black", self.matrix_pos)
