from abc import ABC, abstractmethod


class Player(ABC):
    """
    Abstract class used to represent players

    Public Methods:
        handle_input()

    Instance variables:
        name
        symbol
    """

    @abstractmethod
    def __init__(self, name=None, symbol=None):
        """
        Player class constructor

        Parameters:
            :param name: The name of player object
            :param symbol: The symbol used by player
        """

        self.name = name
        self.symbol = symbol

    @abstractmethod
    def __str__(self):
        return ("\n" + "{0} move!").format(self.name)

    @abstractmethod
    def handle_input(self, board):
        """
        Handles input from players

        Parameters:
            :param board: Game board
        """

        pass
