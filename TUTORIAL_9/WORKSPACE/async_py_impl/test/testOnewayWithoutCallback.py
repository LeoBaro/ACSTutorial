from time import sleep
from Acspy.Clients.SimpleClient import PySimpleClient

client = PySimpleClient()
comp = client.getComponent('ASYNC_PY')

print("before calling delayResult")

comp.delayResultWithOutCallback(3)

print("client: right after delayResult")

sleep(5)

client.releaseComponent(comp.name)

client.disconnect()