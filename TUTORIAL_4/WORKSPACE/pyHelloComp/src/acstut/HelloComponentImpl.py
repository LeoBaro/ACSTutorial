import acstutorial
import acstutorial__POA
import customtypes
import customtypes__POA
  
from Acspy.Servants.ACSComponent import ACSComponent
from Acspy.Servants.ContainerServices import ContainerServices
from Acspy.Servants.ComponentLifecycle import ComponentLifecycle
  
class HelloComponentImpl(acstutorial__POA.HelloComponent, ACSComponent, ContainerServices, ComponentLifecycle):
    
    def __init__(self):
        ACSComponent.__init__(self)
        ContainerServices.__init__(self)
        self._logger = self.getLogger()
    
    def printHi(self):
        print("Just printing 'Hello World!'")
        return

    def getPosition(self):
        p = customtypes.Position(10.0, 5.4)
        return p


    def computeDistance(self, p1, p2):
        return 15.5
    
    def computeCenterOfMass(self):
        return 16.7
