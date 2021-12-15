from Classes.FSM.State import State
from sys import exit


class Exit(State):
    """
    Class used for simulating exit state

    Public Methods:
        play(board, state_machine)
    """

    def play(self, board, state_machine):
        """ Prints exit message and exits from game """
        print("\nThanks for playing! Bye, bye!")
        exit()
