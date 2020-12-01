from time import sleep

from Acspy.Clients.SimpleClient import PySimpleClient

from CALLBACKS_IMPL_MODULE.MyCallbackImpl import MyCallbackImpl

client = PySimpleClient()
comp = client.getComponent('ASYNC_CALLER_PY')

comp.callOneWay()

client.releaseComponent(comp.name)

client.disconnect()