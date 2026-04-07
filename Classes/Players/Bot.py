from Classes.Player import Player


class Bot(Player):
    """
    Class extends Player class, overrides handle_input method. Used for Bot type player.

    Public methods:
        handle_input()
        is_number_char(char)

    Instance variables:
        name
        symbol
    """

    def __init__(self, name=None, symbol=None):
        """ Bot class constructor """
        super().__init__(name, symbol)
        self.opponent_symbol = "O" if symbol == "X" else "X"

    def __str__(self):
        return ("\n" + "{0} move! Please wait...").format(self.name)

    def handle_input(self, board):
        """
        Make turn automatically

        Parameters:
            :param board:
        """
        move = self.__best_move__(board)
        board.update_board(move, self.symbol)

    def __best_move__(self, board):
        """
        Calculate the best move possible

        Parameters:
            :param board: Game board
        """

        # Set default values which going to be overwritten
        best_score = -float("inf")
        best_move = None
        
        alpha = -float("inf")
        beta = float("inf")

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
                
                alpha = max(alpha, best_score)

        return best_move

    def __minimax__(self, board, depth, alpha, beta, maximizing_player):
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
        winner = board.check_winner()
        if winner == self.symbol:
            return 10 - depth
        elif winner == self.opponent_symbol:
            return depth - 10
        elif all(not board.check_availability(i) for i in range(9)):
            return 0

        if maximizing_player:
            max_eval = -float("inf")

            # Check which cells are empty
            for i in range(9):
                if board.check_availability(i):

                    # Check the possible score recursively with own symbol
                    board.board[i] = self.symbol
                    eval_score = self.__minimax__(board, depth + 1, alpha, beta, False)
                    board.board[i] = " "

                    # Check if score we got is better than previous
                    max_eval = max(max_eval, eval_score)
                    alpha = max(alpha, eval_score)
                    
                    if beta <= alpha:
                        break

            return max_eval

        else:
            min_eval = float("inf")

            for i in range(9):
                if board.check_availability(i):
                    board.board[i] = self.opponent_symbol
                    eval_score = self.__minimax__(board, depth + 1, alpha, beta, True)
                    board.board[i] = " "
                    min_eval = min(min_eval, eval_score)
                    beta = min(beta, eval_score)
                    
                    if beta <= alpha:
                        break

            return min_eval