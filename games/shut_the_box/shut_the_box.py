"""Shut-The-Box"""
from itertools import combinations
from random import randint


class Game(object):
    """Run a game of Shut The Box"""
    
    tiles = range(1, 10)
    state = None
    current_roll = 0
    current_total = 0
    current_tiles = []
    
    def roll(self):
        """Roll the dice"""
        self.current_roll = randint(2, 12)
        self.current_total = self.current_roll
    
    @property
    def can_go(self):
        """Determine if there are any legal moves remaining"""
        if self.current_roll in self.tiles:
            return True
        
        for seq_len in range(1, len(self.tiles)):
            for combo in combinations(self.tiles, seq_len):
                if sum(combo) == self.current_roll - self.current_total:
                    return True
        return False
        
    @property
    def possible_plays(self):
        """Determine all possible plays for the given roll"""
        pass
    
    def reset_tiles(self):
        """Flip all tiles to the upright position"""
        self.tiles = range(1, 10)
        
    def reset_play(self):
        """Reset all game state to prepare for a new turn"""
        self.reset_tiles()
        
    def go(self):
        """Manage a players turn. Roll and collect their moves. Determine
        if the game is won based on their selection or if they have reached
        a losing state.
        
        """
        self.roll()
        self.current_tiles = []
        self.current_total = 0
        if self.can_go:
            
            while True:
                print '\nYou rolled %d' % (self.current_roll)
                print "\nTiles Remaining: %s" % self.tiles
                if self.current_tiles:
                    print "Used: %s" % self.current_tiles
                try:
                    pick = raw_input("Flip tile: ")
                except NameError:
                    print "\n\nWhoops!\nPlease select from %s" % self.tiles
                    continue
                if pick > self.current_roll:
                    print "\n%d is bigger than %d! Try again." % \
                            (pick, self.current_roll,)
                    continue
                elif not pick in self.tiles:
                    print "That's not a valid tile"
                    continue
                
                idx = self.tiles.index(pick)
                self.current_tiles.append(self.tiles.pop(idx))
                if not len(self.tiles):
                    self.state = "Win"
                    return False
                self.current_total += pick
                
                print self.current_roll
                print self.current_total
                if self.current_roll == self.current_total:
                    print "------------------\n"
                    return True
                elif not self.can_go:
                    self.current_total = self.current_total + pick
                    self.tiles.insert(idx, pick)
                    print "\nYou cannot finish your turn using that tile. " \
                            "Try again\n"
            
        else:
            print "You rolled %d.\nTiles Left:%s\n Game over." % \
                (self.current_roll, self.tiles,)
            print "Score: %d" % sum(self.tiles)
            self.state = "You rolled %d. \nTiles remaining: %s\nGame over." % \
                         (self.current_roll, self.current_tiles,)
            if raw_input("Play again?").lower() == 'y':
                self.reset_tiles()
                print "\n===============\n"
                return True
            return False
    
    
if __name__ == '__main__':
    game = Game()
    
    print "============================"
    print "   Welcome to Shut The Box"
    print 
   
    while game.go():
        pass
    
    
    
    
    



    
    
    
    





