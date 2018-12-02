import sys
sys.path.append("./lib")

from enum import Enum


class State(Enum):
   Oben = 1
   Unten = 2
   FahreHoch = 3
   FahreRunter = 4
   StopMitte = 5