"""Runs a game of Tic-Tac-Toe"""

from core import IllegalMoveException, PlayerOutOfTurnException

#rows, columns, and diagonals
R1 = (0,1,2,)
R2 = (3,4,5,)
R3 = (6,7,8,)
C1 = (0,3,6,)
C2 = (1,4,7,)
C3 = (2,5,8,)
D1 = (0,4,8,)
D2 = (2,4,6,)
WIN_CHECKS = {0:[R1,C1,D1],
              1:[R1,C2],
              2:[R1,C3,D2],
              3:[R2,C1],
              4:[R2,C2,D1,D2],
              5:[R2,C3],
              6:[R3,C1,D2],
              7:[R3,C2],
              8:[R3,C3,D1]}


def create_game():
    """Initialize a new game
    
    The grid is indexed as:
    0 1 2
    3 4 5
    6 7 8
    
    >>> create_game()
    {'state': [False, False, False, False, False, False, False, False, False], 'moves': []}
    """
    return {'state':[False]*9,
            'moves':[]}

def go(square,play,game_state=None):
    """updates the game state with a move
    
    move: (square, play)
    
    >>> from tic_tac_toe import create_game, go
    >>> winner,state = go(0,'X')
    >>> winner
    >>> state
    {'state': ['X', False, False, False, False, False, False, False, False], 'moves': [(0, 'X')]}
    >>> winner,state = go(0,'X',state)
    ------------------------------------------------------------
    Traceback (most recent call last):
      File "<ipython console>", line 1, in <module>
      File "tic_tac_toe.py", line 50, in go
        raise IllegalMoveException("Square is already taken.")
    IllegalMoveException: Square is already taken.
    
    >>> winner,state = go(1,'X',state)
    ------------------------------------------------------------
    Traceback (most recent call last):
      File "<ipython console>", line 1, in <module>
      File "tic_tac_toe.py", line 54, in go
        raise PlayerOutOfTurnException
    PlayerOutOfTurnException
    
    >>> winner,state = go(1,'O',state)
    >>> winner
    >>> state
    {'state': ['X', 'O', False, False, False, False, False, False, False], 'moves': [(0, 'X'), (1, 'O')]}
    >>> winner,state = go(3,'X',state)
    >>> winner
    >>> state
    {'state': ['X', 'O', False, 'X', False, False, False, False, False], 'moves': [(0, 'X'), (1, 'O'), (3, 'X')]}
    >>> winner,state = go(2,'O',state)
    >>> wi    >>> create_game()
    ------------------------------------------------------------
       File "<ipython console>", line 1
         wi    >>> create_game()
                 ^
    SyntaxError: invalid syntax
    
    >>>     {'state': [False, False, False, False, False, False, False, False, False], 'moves': []}
    ... 
    {'state': [False, False, False, False, False, False, False, False, False], 'moves': []}
    >>> winner,state = go(2,'O',state)
    ------------------------------------------------------------
    Traceback (most recent call last):
      File "<ipython console>", line 1, in <module>
      File "tic_tac_toe.py", line 50, in go
        raise IllegalMoveException("Square is already taken.")
    IllegalMoveException: Square is already taken.
    
    >>> winner
    >>> state
    {'state': ['X', 'O', 'O', 'X', False, False, False, False, False], 'moves': [(0, 'X'), (1, 'O'), (3, 'X'), (2, 'O')]}



    >>> from tic_tac_toe import create_game, go
    >>> go(0,1)
    (None, {'state': [1, False, False, False, False, False, False, False, False], 'moves': [(0, 1)]})
    >>> winner,state = go(1,2,_[1])
    >>> winner,state = go(3,1,_[1])
    >>> winner,state = go(2,2,_[1])
    >>> winner,state = go(6,1,_[1])

    """
    
    if game_state == None:
        game_state = create_game()    
    state = game_state['state']
    
    #make sure the square is not already taken
    if state[square]:
        raise IllegalMoveException("Square is already taken.")
        
    #player cannot play twice consecutively
    if len(game_state['moves']) and game_state['moves'][-1][1] == play:
        raise PlayerOutOfTurnException
        
    #update game state
    state[square] = play
    game_state['moves'].append((square,play,))
    for check in WIN_CHECKS[square]:
        if state[check[0]] == play and \
           state[check[1]] == play and \
           state[check[2]] == play:
            return play,game_state
    return None,game_state
    
    