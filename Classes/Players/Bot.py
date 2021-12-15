from Classes.Player import Player


class Bot(Player):
    """
    Class extends Player class, overrides handle_input method. Used for Bot type player.

    Public methods:
        handle_input()
        is_number_char(char)

    Instance variables:
        __best_symbol
        name
        symbol
    """

    __best_symbol = None

    def __init__(self, name=None, symbol=None):
        """ Bot class constructor """
        super().__init__(name, symbol)

    def __str__(self):
        return ("\n" + "{0} move! Please wait...").format(self.name)

    def handle_input(self, board):
        """
        Make turn automatically

        Parameters:
            :param board:
        """

        board.update_board(self.__best_move__(board), self.__best_symbol)

    def __best_move__(self, board):
        """
        Calculate the best move possible

        Parameters:
            :param board: Game board
        """

        # Set default values which going to be overwritten
        best_score = -1001
        best_move = 0
        alpha, beta = -1000, 1000

        # Check which cells are empty
        for i in range(9):
            if board.check_availability(i):

                # Set each empty board cell and check the possible score and set board value back
                board.board[i] = self.symbol
                score = self.__minimax__(board, 0, alpha, beta, False)
                board.board[i] = " "

                # High score achieved, save the value and position
                if score > best_score:
                    best_score = score
                    best_move = i
                    self.__best_symbol = self.symbol

        for i in range(9):
            if board.check_availability(i):

                # Set each empty board cell and check the possible score and set board value back
                board.board[i] = "X"
                score = self.__minimax__(board, 0, alpha, beta, False)
                board.board[i] = " "

                # High score achieved, save the value and position
                if score > best_score:
                    best_score = score
                    best_move = i
                    self.__best_symbol = "X"

        return best_move

    def __minimax__(self, board, depth, alpha, beta, maximize):
        """
        Minimax with alpha-beta prunning algorithm function (adapted)
        Source: https://github.com/GeorgeSeif/Tic-Tac-Toe-AI/blob/master/Source.cpp

        Parameters:
            :param board: Game board
            :param depth: Recursion depth
            :param depth: Alpha
            :param depth: Beta
            :param maximize: AI move or player move
        """

        # Check if any board state occurs, if so gives it a score
        result = board.check_winner()
        if result:
            if not maximize:
                return 1000
            else:
                return -1000

        # If bot move - need to maximize the efficiency of move
        if maximize:
            best_score = -1000

            # Check which cells are empty
            for i in range(9):
                if board.check_availability(i):

                    # Check the possible score recursively with own symbol
                    board.board[i] = self.symbol
                    score = self.__minimax__(board, depth + 1, alpha, beta, False)
                    board.board[i] = " "

                    # Check if score we got is better than previous
                    if score > best_score:
                        best_score = score - depth * 10
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break

            # Check which cells are empty with different symbol
            for i in range(9):
                if board.check_availability(i):

                    # Check the possible score recursively with own symbol
                    board.board[i] = "X"
                    score = self.__minimax__(board, depth + 1, alpha, beta, False)
                    board.board[i] = " "

                    # Check if score we got is better than previous
                    if score > best_score:
                        best_score = score - depth * 10
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break

            return best_score

        # Predict how player will make a move in best scenario
        else:
            best_score = 1000

            # Check which cells are empty
            for i in range(9):
                if board.check_availability(i):

                    # Check the possible score recursively
                    board.board[i] = "X"
                    score = self.__minimax__(board, depth + 1, alpha, beta, True)
                    board.board[i] = " "

                    if score < best_score:
                        best_score = score + depth * 10
                        beta = min(score, best_score)
                        if beta <= alpha:
                            break

            # Check which cells are empty with different symbol
            for i in range(9):
                if board.check_availability(i):

                    # Check the possible score recursively
                    board.board[i] = self.symbol
                    score = self.__minimax__(board, depth + 1, alpha, beta, True)
                    board.board[i] = " "

                    if score < best_score:
                        best_score = score + depth * 10
                        beta = min(score, best_score)
                        if beta <= alpha:
                            break

            return best_score
