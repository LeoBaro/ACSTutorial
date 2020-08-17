import acstutorial
import acstutorial__POA
import acstut
import CUSTOMErr
import CUSTOMErrImpl

from Acspy.Servants.ACSComponent import ACSComponent
from Acspy.Servants.ContainerServices import ContainerServices
from Acspy.Servants.ComponentLifecycle import ComponentLifecycle


class ConsoleImpl(acstutorial__POA.Console, ACSComponent, ContainerServices, ComponentLifecycle):
    def __init__(self):
        ACSComponent.__init__(self)
        ContainerServices.__init__(self)
        self._logger = self.getLogger()


    def setTelescopePosition(self,x, y):
        telescope_comp = self.getComponent("PY_TELESCOPE")
        try:
            telescope_comp.moveTo(x, y)
        except CUSTOMErr.PositionOutOfLimitsEx as e:
            print("PositionOutOfLimits exception caught")
        self.releaseComponent("PY_TELESCOPE")

    def getTelescopePosition(self):
        telescope_comp = self.getComponent("PY_TELESCOPE")
        s = telescope_comp.getCurrentPosition()
        self.releaseComponent("PY_TELESCOPE")
        return s
        
        