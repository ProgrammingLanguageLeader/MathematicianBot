from enum import Enum, unique


@unique
class ConversationStates(Enum):
    SIMPLE_MODE = 0
    DETAILED_MODE = 1
