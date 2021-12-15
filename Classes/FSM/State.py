from abc import ABC, abstractmethod


class State(ABC):
    """
    Abstract class used for simulating gaming states

    Public Methods:
        play(board, state_machine)
    """

    def __init__(self):
        """ State class constructor """
        pass

    @abstractmethod
    def play(self, board, state_machine):
        """
        Handles specific state behaviour

        Parameters:
            :param board:
            :param state_machine:
        """
        pass
