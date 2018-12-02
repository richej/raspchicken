from enum import Enum

@unique
class State(Enum):
   Oben = 1
   Unten = 2
   FahreHoch = 3
   FahreRunter = 4
   StopMitte = 5