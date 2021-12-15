
class StateMachine:
    """
    Class used to create state machine

    Public Methods:
        change_state(new_state)

    Instance variables:
        current_state
    """

    def __init__(self, initial_state=None):
        """ StateMachine class constructor """
        self.current_state = initial_state

    def change_state(self, new_state=None):
        """ Change current state """
        self.current_state = new_state
