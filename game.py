import collections
import sys
import os

Note = collections.namedtuple('Note', ['time', 'pos'])
Song = collections.namedtuple('Song', ['mp3', 'notes'])

def write_at(x, y, text):
    sys.stdout.write('\x1b7\x1b[%d;%df%s\x1b8' % (y, x, text))
    sys.stdout.flush()

class Game:
    def __init__(self):
        self.load_songs()
        
    def load_songs(self):
        pass

    def clear_screen(self):
        os.system('clear')

    def draw_board(self):
        x, y, width, height = 0, 0, 30, 40
        
        for cur_y in range(y+1, y+height+2):
            write_at(x+1, cur_y, '|')
            write_at(x+width+1, cur_y, '|')

game = Game()
game.clear_screen()
game.draw_board()
