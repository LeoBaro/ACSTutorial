import AsyncModule
import AsyncModule__POA

from time import sleep
import random

from Acspy.Servants.ACSComponent import ACSComponent
from Acspy.Servants.ContainerServices import ContainerServices

from CALLBACKS_IMPL_MODULE.MyCallbackImpl import MyCallbackImpl


class AsyncExampleCallerImpl(AsyncModule__POA.AsyncExampleCaller, ACSComponent, ContainerServices):

    def __init__(self):
        ACSComponent.__init__(self)
        ContainerServices.__init__(self)
        self._logger = self.getLogger()

    def callOneWay(self):

        self._logger.logInfo("[AsyncExampleCallerImpl - callOneWay] start!")

        asyncComp = self.getComponent("ASYNC_PY")

        cb = MyCallbackImpl()

        from Acspy.Clients.SimpleClient import PySimpleClient
        client = PySimpleClient()
        cbObj = client.activateOffShoot(cb)
        
        #cbObj = self.activateOffShoot(cb)

        self._logger.logInfo("[AsyncExampleCallerImpl - callOneWay] before calling delayResult")
        cbData = cb.get()
        self._logger.logInfo("cb.get: %s %s"%(cbData.status, cbData.data))
        
        asyncComp.delayResult(6, cbObj)

        self._logger.logInfo("[AsyncExampleCallerImpl - callOneWay] right after calling delayResult")
        cbData = cb.get()
        self._logger.logInfo("[AsyncExampleCallerImpl - callOneWay] cb.get: %s %s"%(cbData.status, cbData.data))
      
        sleep(1)

        self._logger.logInfo("[AsyncExampleCallerImpl - callOneWay] 1 sec after delayResult")
        cbData = cb.get()
        self._logger.logInfo("[AsyncExampleCallerImpl - callOneWay] cb.get: %s %s"%(cbData.status, cbData.data))

        sleep(8)

        self._logger.logInfo("[AsyncExampleCallerImpl - callOneWay] after 8 sec sleep ")
        cbData = cb.get()
        self._logger.logInfo("[AsyncExampleCallerImpl - callOneWay] cb.get: %s %s"%(cbData.status, cbData.data))


        self.releaseComponent(asyncComp.name)

        client.disconnect()