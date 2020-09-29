import acstutorial
import acstutorial__POA

  
from Acspy.Servants.ACSComponent import ACSComponent
from Acspy.Servants.ContainerServices import ContainerServices
from Acspy.Servants.ComponentLifecycle import ComponentLifecycle

from Acspy.Nc.Consumer import Consumer

import NC_DEFINITIONS_MODULE

class ConsumerCompImpl(acstutorial__POA.ConsumerComp, ACSComponent, ContainerServices, ComponentLifecycle):
    
    def __init__(self):
        ACSComponent.__init__(self)
        ContainerServices.__init__(self)
        self._logger = self.getLogger()
        self.con = None
        
    def eventHandler(self, event):
        self._logger.logInfo("New messsage received: " + str(event))

            
    def initialize(self):
        self.con = Consumer(NC_DEFINITIONS_MODULE.CHANNELNAME_EXAMPLE)


    def execute(self):
        self.con.addSubscription(NC_DEFINITIONS_MODULE.ExampleEvent, self.eventHandler)
        self.con.consumerReady()

    def cleanUp(self):
        self.con.disconnect()

    def aboutToAbort(self):
        pass

