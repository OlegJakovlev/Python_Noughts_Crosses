from random import randint
from Classes.FSM.States.ExitState import Exit
from Classes.FSM.States.StartState import Start
from Classes.FSM.State import State
from Classes.Players.Bot import Bot
from Classes.Players.Human import Human


class Menu(State):
    """
    Class used for simulating menu state

    Public Methods:
        play(board, state_machine)
    """

    def play(self, board, state_machine):
        """ Output welcome screen and waits mode to be selected """
        self.__welcome_screen__()
        self.__select_mode__(state_machine)

    @staticmethod
    def __select_mode__(state_machine):
        """ Validate input and set player mode/exit """
        while True:
            mode = input()
            if len(mode) == 1 and "1" <= mode <= "3":
                mode = int(mode)
                break
            else:
                print("Wrong input!\n")

        # If user want to exit we don't need to run other part of the program
        if mode == 3:
            state_machine.change_state(Exit())
        else:
            # By default set players as Human vs Bot, if mode == 2 set to Human vs Human
            player_1 = Human("Player 1", "X")
            player_2 = Bot("Bot", "O") if mode == 1 else Human("Player 2", "O")

            # Choose who will have first move
            first_player_flag = randint(0, 1)

            # After we got players, begin the game
            state_machine.change_state(Start(player_1, player_2, first_player_flag))

    @staticmethod
    def __welcome_screen__():
        """ Prints welcome screen """

        print("""
        Welcome to: 
        
         ________  __                  ________                            ________                     
        /        |/  |                /        |                          /        |                    
        $$$$$$$$/ $$/   _______       $$$$$$$$/   ______    _______       $$$$$$$$/   ______    ______  
           $$ |   /  | /       |         $$ |    /      \  /       |         $$ |    /      \  /      \ 
           $$ |   $$ |/$$$$$$$/          $$ |    $$$$$$  |/$$$$$$$/          $$ |   /$$$$$$  |/$$$$$$  |
           $$ |   $$ |$$ |               $$ |    /    $$ |$$ |               $$ |   $$ |  $$ |$$    $$ |
           $$ |   $$ |$$ \_____          $$ |   /$$$$$$$ |$$ \_____          $$ |   $$ \__$$ |$$$$$$$$/ 
           $$ |   $$ |$$       |         $$ |   $$    $$ |$$       |         $$ |   $$    $$/ $$       |
           $$/    $$/  $$$$$$$/          $$/     $$$$$$$/  $$$$$$$/          $$/     $$$$$$/   $$$$$$$/ 

        FAQ:
            1. How do I place figure?
            - You need to write <number_of_cell> <X/O>
            Example: 2 X
            Example: 9 O
            
            2. How do I move figure?
            - You need to write </move> <Position_To_Move_From> <Position_To_Move_To>
            Example: /move 2 4
            Example: /move 1 9
            
            3. Who move first?
            - It depends on random
            
        Additional rules:
            1. Each player can place either X and O symbols
            2. If win combination is found - wins who placed the last symbol

        Menu:
            1. Human vs Bot
            2. Human vs Human
            3. Exit
            
        @Copyright by Olegs Jakovlevs
        """)
