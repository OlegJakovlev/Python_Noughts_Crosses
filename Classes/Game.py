from Classes.FSM.States.DrawState import Exit
from Classes.FSM.States.MenuState import Menu
from Classes.Board import Board
from Classes.FSM.StateMachine import StateMachine


class Game:
    """
    Class used to handle game process

    Instance variables:
        __board
        __state_machine
    """

    def __init__(self):
        """ Creates board, state_machine and run the game """
        self.__board = Board(7)  # Width as parameter
        self.__state_machine = StateMachine(Menu())

        # Run the game
        while self.__state_machine.current_state != Exit:
            self.__state_machine.current_state.play(self.__board, self.__state_machine)
