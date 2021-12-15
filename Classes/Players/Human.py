from Classes.Player import Player


class Human(Player):
    """
    Class extends Player class, overrides handle_input method. Used for Human type player

    Public Methods:
        handle_input()
        is_number_char(char)

    Instance variables:
        name
        symbol
    """

    def __init__(self, name, symbol):
        """ Human class constructor """
        super().__init__(name, symbol)

    def __str__(self):
        return super().__str__()

    def handle_input(self, board):
        """
        Get command, checks its length and if data provided is valid

        Parameters:
            :param board: Game board
        """

        made_move = False

        while not made_move:
            board.print_board()

            # Get input
            command = input("Enter the move:\t")

            # Check if we can split the string given
            if len(command) != 0:
                command = command.split()

                #   If length is 3 it should be /move method with 2 numbers (from 1 to 9) provided
                if len(command) == 3:
                    # Check if input was /move and 2 numbers
                    if command[0] == "/move" and len(command[1]) == len(command[2]) == 1 \
                            and command[1] != command[2] and self.is_number_char(command[1]) \
                            and self.is_number_char(command[2]):

                        # Check if move element executed properly
                        if board.move_element(int(command[1]) - 1, int(command[2]) - 1):
                            made_move = True
                    else:
                        print("Invalid input!\n")

                #   If length is 2 it should be insert method with 1 number (from 1 to 9) provided
                elif len(command) == 2:
                    if len(command[0]) == len(command[-1]) == 1 and self.is_number_char(command[0]) and command[-1].capitalize() in "XO":
                        if board.update_board(int(command[0]) - 1, command[-1].capitalize()):
                            made_move = True
                    else:
                        print("Invalid input!\n")
                else:
                    print("Invalid input!\n")
            else:
                print("Invalid input!\n")

    @staticmethod
    def is_number_char(char):
        """ Checks if provided char is number between 1 and 9

        Parameters:
            :param char: Symbol to be checked
        """

        return "1" <= char <= "9"

