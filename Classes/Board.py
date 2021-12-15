class Board:
    """
    Class used to handle game board and game logic

    Public Methods:
        print_board()
        check_availability(position)
        update_board(position, marker)
        check_winner(player1, player2)
        move_element(from_where, to_where)
        check_draw()

    Instance variables:
        board
        __width
    """

    def __init__(self, width=None):
        """
        Board class constructor

        Parameters:
            :param width: Visual width of board
        """
        self.board = list([" " for i in range(9)])  # Initialize list with empty strings
        self.__width = width

    def __str__(self):
        """ Function which prints game board """
        return ("\n"+"\n".join(
            ["|".join(
                [("{0:^" + str(self.__width) + "}").format(self.board[row * 3 + column]) for column in
                 range(3)])  # Vertical elements
             + "\n" +
             ("_" * (self.__width * 3 + 2) if row < 2 else "") for row in range(3)]))  # Horizontal elements

    def print_board(self):
        print(self)

    def check_availability(self, position):
        """ Checks if board at given position is empty """
        return self.board[position] == " "

    def update_board(self, position, marker):
        """
        Checks if board position is empty and enters a marker there

        Parameters:
            :param position: Position on board
            :param marker: Symbol to be placed
        """

        # Check if board at position is empty
        if self.check_availability(position):
            self.board[position] = marker
        else:
            print("There is something else! Please use empty fields!\n")
            return False

        self.print_board()
        return True

    def check_winner(self):
        """
        Get winner by combinations:
            1. Columns
            2. Rows
            3. Diagonals
        Or no winner
        """

        # Check rows
        for row in range(3):
            position = row * 3
            if self.board[position] == self.board[position + 1] == self.board[position + 2] != " ":
                return True

        # Check columns
        for column in range(3):
            if self.board[column] == self.board[column + 3] == self.board[column + 6] != " ":
                return True

        """
        Check 2 diagonals:
        
        1. From left to right
        x . .
        . x .
        . . x
        
        2. From right to left
        . . x
        . x .
        x . .
        """

        # From left to right diagonal
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True

        # From right to left diagonal
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True

        # There is no winner
        return False

    def move_element(self, from_where, to_where):
        """
        Move element to a new position if is empty

        Parameters:
            :param from_where:
            :param to_where:
        """

        # Switch element position
        if self.board[from_where] in "XO" and self.board[to_where] == " ":
            self.board[from_where], self.board[to_where] = self.board[to_where], self.board[from_where]
        else:
            print("\nYou selected wrong start/end position! Please check once more!")
            return False
        return True

    def check_draw(self):
        """ Function checks if on board are any empty fields, if no - it is draw """
        for i in self.board:
            if i == " ":
                return False
        return True
