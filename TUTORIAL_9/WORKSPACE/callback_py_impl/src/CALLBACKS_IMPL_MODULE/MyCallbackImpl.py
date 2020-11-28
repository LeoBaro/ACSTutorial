import AsyncModule
import AsyncModule__POA

class CallbackStatus:
    INIT = 0
    WORKING = 1
    DONE = 2

    @staticmethod
    def get(code):
        if code == 0:
            return "INIT"
        elif code == 1:
            return "WORKING"
        elif code == 2:
            return "DONE"

class MyCallbackImpl(AsyncModule__POA.MyCallback):
    
    def __init__(self):
        self.status = CallbackStatus.get(CallbackStatus.INIT)
        self.data = None

    def working(self, data):
        self.status = CallbackStatus.get(CallbackStatus.WORKING)
        self.data = data

    def done(self, data):
        self.status = CallbackStatus.get(CallbackStatus.DONE)
        self.data = data
    
    def get(self):
        return AsyncModule.CallbackInfo(self.status, self.data)
        