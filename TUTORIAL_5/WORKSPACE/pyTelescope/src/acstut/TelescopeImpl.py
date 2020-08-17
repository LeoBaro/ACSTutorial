import acstutorial
import acstutorial__POA
import acstut
import CUSTOMErr
import CUSTOMErrImpl
  
from Acspy.Servants.ACSComponent import ACSComponent
from Acspy.Servants.ContainerServices import ContainerServices
from Acspy.Servants.ComponentLifecycle import ComponentLifecycle
  
class TelescopeImpl(acstutorial__POA.Telescope, ACSComponent, ContainerServices, ComponentLifecycle):
    def __init__(self):
        ACSComponent.__init__(self)
        ContainerServices.__init__(self)
        self._logger = self.getLogger()
        self.x = 0
        self.y = 0

    def printHello(self):
        print("Just printing 'Hello World!'")
        return "Hello World!"

    def moveTo(self, x, y):

        if x < 0 or y < 0:
            raise CUSTOMErrImpl.PositionOutOfLimitsExImpl()
        self.x = x
        self.y = y
    
    def getCurrentPosition(self):
        print("Telescope current position in x:" + str(self.x)+ "y: " + str(self.y))
        return "Telescope in: x: " + str(self.x) + " y: " + str(self.y)

