from game.casting.actor import Actor

# coppied from the rfk assignment earlier this week
# No chnages needed (Zack D.)

# I do not think this classes is needed, but due to other files calling the parent funciton through the child function it cannot be removed. 
# We also are required to have 8 classes for this assignment and this class helps us complete that requirment. (Zack D.)

# I think we can add something to the code that will use this class to congragulate the player when they get a gem and to tell them they suck if they get a rock (Zack D.)

class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        
    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message
