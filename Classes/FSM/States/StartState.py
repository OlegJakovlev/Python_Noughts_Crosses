from Classes.FSM.State import State
from Classes.FSM.States.DrawState import Draw
from Classes.FSM.States.WinState import Win


class Start(State):
    """
    Class used for simulating win state

    Public Methods:
        play(board, state_machine)

    Instance variables:
        __player_flag
        __player1
        __player2
    """

    def __init__(self, player1=None, player2=None, first_move=None):
        """ Start state constructor """
        self.__player_flag = first_move
        self.__player1 = player1
        self.__player2 = player2

    def play(self, board, state_machine):
        """ Handles moves logic, checks winner & draw """
        # Depending of flag game decide which player move is now
        if self.__player_flag:
            print(self.__player1)
            self.__player1.handle_input(board)
        else:
            print(self.__player2)
            self.__player2.handle_input(board)

        # Check if on board there is winning combination
        if board.check_winner():
            if self.__player_flag:
                state_machine.change_state(Win(self.__player1.name))
                return
            else:
                state_machine.change_state(Win(self.__player2.name))
                return

        # If after last symbol entered there is no winning combination - it must be draw
        if board.check_draw():
            state_machine.change_state(Draw())
            return

        # Change current player move
        self.__player_flag = not self.__player_flag
