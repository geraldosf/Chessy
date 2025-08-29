from dataclasses import *
from objects.pieces import *
from pygame import rect

@dataclass
class chess_pos:

    label: str
    pos: tuple
    image_pos: tuple = field(init=False)
    height: int
    width: int
    rect: object = field(init=False)
    piece:object = None

    def __post_init__(self):

        self.image_pos = (self.pos[0] - 15, self.pos[1] - 15)
        self.rect = (self.pos[0], self.pos[1], self.height, self.width)


        if self.label == "a1" or self.label == "h1":
            self.piece = rook("white")
        elif self.label == "b1" or self.label == "g1":
            self.piece = knight("white")
        elif self.label == "c1" or self.label == "f1":
            self.piece = bishop("white")
        elif self.label == "d1":
            self.piece = queen("white")
        elif self.label == "e1":
            self.piece = king("white")
        else:
            for i in range(8):
                if self.label == chr(ord(self.label[0]) + i) + "2":
                    self.piece = pawn("white")


        if self.label == "a8" or self.label == "h8":
            self.piece = rook("black")
        elif self.label == "b8" or self.label == "g8":
            self.piece = knight("black")
        elif self.label == "c8" or self.label == "f8":
            self.piece = bishop("black")
        elif self.label == "d8":
            self.piece = queen("black")
        elif self.label == "e8":
            self.piece = king("black")
        else:
            for i in range(8):
                if self.label == chr(ord(self.label[0]) + i) + "7":
                    self.piece = pawn("black")


