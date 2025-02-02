"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def __init__(self, player):
        self.player = player
        self._has_moved = False
    
    def get_available_moves(self, board):
        current_position = board.find_piece(self)
        player_move = 1 if self.player == Player.WHITE else -1
        possible_positions = []

        new_move = Square.at(current_position.row + player_move, current_position.col)
        if(board.inbounds(new_move) and board.space_available(self.player, new_move)):
            possible_positions.append(new_move)
            new_move = Square.at(current_position.row + player_move * 2, current_position.col)
            if (board.inbounds(new_move) and not self._has_moved and board.space_available(self.player, new_move)):
                possible_positions.append(new_move)
        return possible_positions

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)
        self._has_moved = True


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []