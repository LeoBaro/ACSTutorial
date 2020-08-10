import acstutorial
import acstutorial__POA
import acstut
  
from Acspy.Servants.ACSComponent import ACSComponent
from Acspy.Servants.ContainerServices import ContainerServices
from Acspy.Servants.ComponentLifecycle import ComponentLifecycle


class ConsoleImpl(acstutorial__POA.Console, ACSComponent, ContainerServices, ComponentLifecycle):
    def __init__(self):
        ACSComponent.__init__(self)
        ContainerServices.__init__(self)
        self._logger = self.getLogger()


    def setTelescopePosition(self,x, y):
        telescope_comp = self.getComponent("CPP_TELESCOPE")
        telescope_comp.moveTo(x, y)
        self.releaseComponent("CPP_TELESCOPE")

    def getTelescopePosition(self):
        telescope_comp = self.getComponent("CPP_TELESCOPE")
        s = telescope_comp.getCurrentPosition()
        self.releaseComponent("CPP_TELESCOPE")
        return s
        
        