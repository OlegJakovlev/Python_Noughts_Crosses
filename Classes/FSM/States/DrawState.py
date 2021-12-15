from Classes.FSM.States.ExitState import Exit
from Classes.FSM.State import State


class Draw(State):
    """
    Class used for simulating draw state

    Public Methods:
        play(board, state_machine)
    """

    def play(self, board, state_machine):
        """ Prints draw message and exits the game """
        print("There is no winner! DRAW!")
        state_machine.change_state(Exit())
