from Classes.FSM.States.ExitState import Exit
from Classes.FSM.State import State


class Win(State):
    """
    Class used for simulating win state

    Public Methods:
        play(board, state_machine)

    Instance variables:
        __winner
    """

    def __init__(self, winner=None):
        """ Win state constructor """
        self.__winner = winner

    def play(self, board, state_machine):
        """ Prints win message and exit the game """
        print(self.__winner+" wins the game!")
        state_machine.change_state(Exit())
