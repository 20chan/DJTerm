import collections
import sys
import os

Note = collections.namedtuple('Note', ['time', 'pos'])
Song = collections.namedtuple('Song', ['mp3', 'notes'])

screen_size = os.popen('stty size', 'r').read().split()
screen_size = [int(x) for x in screen_size][::1]

def write_at(x, y, text):
    sys.stdout.write('\x1b7\x1b[%d;%df%s\x1b8' % (y, x, text))
    sys.stdout.flush()

class Game:
    def __init__(self):
        self.load_songs() 
        self.x, self.y, self.width, self.height = 0, 0, 30, screen_size[1] - 5
    def load_songs(self):
        pass

    def clear_screen(self):
        # os.system('clear')
        print('\n' * screen_size[1])

    def draw_board(self):
        for cur_y in range(self.y+1, self.y+self.height+2):
            write_at(self.x+1, cur_y, '|')
            write_at(self.x+self.width+1, cur_y, '|')

game = Game()
game.clear_screen()
game.draw_board()
