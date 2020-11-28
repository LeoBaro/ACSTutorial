import AsyncModule
import AsyncModule__POA

from time import sleep
import random

from Acspy.Servants.ACSComponent import ACSComponent
from Acspy.Servants.ContainerServices import ContainerServices



class AsyncExampleImpl(AsyncModule__POA.AsyncExample, ACSComponent, ContainerServices):

    def __init__(self):
        ACSComponent.__init__(self)
        ContainerServices.__init__(self)
        self._logger = self.getLogger()

    def delayResultWithOutCallback(self, sleepSec):

        self._logger.logInfo("[AsynExampleImpl - delayResultWithOutCallback] start!")
        
        sleep(sleepSec)
        
        self._logger.logInfo("[AsynExampleImpl - delayResultWithOutCallback] finish!")


    def delayResult(self, sleepSec, stringCallback):
        
        self._logger.logInfo("[AsynExampleImpl - delayResult] start!")

        stringCallback.working("DATA")

        sleep(sleepSec)

        stringCallback.done("DATA")

        self._logger.logInfo("[AsynExampleImpl - delayResult] almost finished, setting the callback!")

        self._logger.logInfo("[AsynExampleImpl - delayResult] finish!")
