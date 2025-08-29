from dataclasses import *
from pygame import image


@dataclass
class king:

    side: str
    Image: object = field(init=False)

    def __post_init__(self):
        if self.side == "white":
            self.Image = image.load("pieces_image/white-king.png")
        elif self.side == "black":
            self.Image = image.load("pieces_image/black-king.png")

        

@dataclass
class queen():
    
    side: str
    Image: object = field(init=False)

    def __post_init__(self):
        if self.side == "white":
            self.Image = image.load("pieces_image/white-queen.png")
        elif self.side == "black":
            self.Image = image.load("pieces_image/black-queen.png")


@dataclass
class knight():

    side: str
    Image: object = field(init=False)

    def __post_init__(self):
        if self.side == "white":
            self.Image = image.load("pieces_image/white-knight.png")
        elif self.side == "black":
            self.Image = image.load("pieces_image/black-knight.png")


@dataclass  
class bishop():

        side: str
        Image: object = field(init=False)

        def __post_init__(self):
            if self.side == "white":
                self.Image = image.load("pieces_image/white-bishop.png")
            elif self.side == "black":
                self.Image = image.load("pieces_image/black-bishop.png")

@dataclass   
class rook():

    side: str
    Image: object = field(init=False)

    def __post_init__(self):
        if self.side == "white":
            self.Image = image.load("pieces_image/white-rook.png")
        elif self.side == "black":
            self.Image = image.load("pieces_image/black-rook.png")


@dataclass
class pawn():
        
    side: str
    Image: object = field(init=False)

    def __post_init__(self):
        if self.side == "white":
            self.Image = image.load("pieces_image/white-pawn.png")
        elif self.side == "black":
            self.Image = image.load("pieces_image/black-pawn.png")


    
