import acstutorial
import acstutorial__POA
  
from Acspy.Servants.ACSComponent import ACSComponent
from Acspy.Servants.ContainerServices import ContainerServices
from Acspy.Servants.ComponentLifecycle import ComponentLifecycle

from Acspy.Nc.Supplier import Supplier

import NC_DEFINITIONS_MODULE

class SupplierCompImpl(acstutorial__POA.SupplierComp, ACSComponent, ContainerServices, ComponentLifecycle):
    
    def __init__(self):
        ACSComponent.__init__(self)
        ContainerServices.__init__(self)
        self._logger = self.getLogger()
        self.sup = None

            
    def initialize(self):
        self.sup = Supplier(NC_DEFINITIONS_MODULE.CHANNELNAME_EXAMPLE)


    def execute(self):
        #Retrieve components
        #Consider ready to receive calls (Change states if appropriate)
        pass

    def cleanUp(self):
        self.sup.disconnect()

    def aboutToAbort(self):
        #Do any critical clean up
        #Continue with less critical stuff such as releasing components and other activities similar to cleanUp
        pass


    def sendEvent(self):
        event = NC_DEFINITIONS_MODULE.ExampleEvent("MessageKey", 10)
        self._logger.logInfo("Publishing event.." + str(event))
        self.sup.publishEvent(simple_data=event)
        

