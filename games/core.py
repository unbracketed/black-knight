class IllegalMoveException(Exception):
    """Indicates that a requested move/play would violate the rules of the game."""
    pass


class PlayerOutOfTurnException(Exception):
    """Indicates that the player requesting a move/play is not permitted to do
    so until at least one other player has made a move.
    
    """
    pass