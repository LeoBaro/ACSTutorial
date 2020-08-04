import acstutorial
import acstutorial__POA
  
from Acspy.Servants.ACSComponent import ACSComponent
from Acspy.Servants.ContainerServices import ContainerServices
from Acspy.Servants.ComponentLifecycle import ComponentLifecycle
  
class HelloComponentImpl(acstutorial__POA.HelloComponent, ACSComponent, ContainerServices, ComponentLifecycle):
    def __init__(self):
        ACSComponent.__init__(self)
        ContainerServices.__init__(self)
        self._logger = self.getLogger()
    def printHello(self):
        print("Just printing 'Hello World!'")
        return "Hello World!"
