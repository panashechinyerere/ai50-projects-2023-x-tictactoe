class TicTacToe:
    def _init_(self):
        self.X = 'X'
        self.O = 'O'
        self.EMPTY = ''

        self.board = self.initial_state()

    def initial_state(self):
        return [[self.EMPTY, self.EMPTY, self.EMPTY],
                [self.EMPTY, self.EMPTY, self.EMPTY],
                [self.EMPTY, self.EMPTY, self.EMPTY]]

    def make_move(self, mouse_pos):
        row = mouse_pos[1] // 100
        col = mouse_pos[0] // 100
        if self.board[row][col] == self.EMPTY:
            self.board[row][col] = self.player()

    def player(self):
        count_X = sum(row.count(self.X) for row in self.board)
        count_O = sum(row.count(self.O) for row in self.board)
        return self.X if count_X <= count_O else self.O