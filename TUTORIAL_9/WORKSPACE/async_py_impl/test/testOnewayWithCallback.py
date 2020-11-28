from time import sleep

from Acspy.Clients.SimpleClient import PySimpleClient

from CALLBACKS_IMPL_MODULE.MyCallbackImpl import MyCallbackImpl

client = PySimpleClient()
comp = client.getComponent('ASYNC_PY')

cb = MyCallbackImpl()

cbObj = client.activateOffShoot(cb)

print("before calling delayResult")
print("cb.get", cb.get())
comp.delayResult(3, cbObj)

print("client: right after delayResult")
print("cb.get", cb.get())

sleep(1)

print("client: 1 sec after delayResult")
print("cb.get", cb.get())

sleep(3)

print("client: after 7 sec sleep ")
print("cb.get", cb.get())

client.releaseComponent(comp.name)

client.disconnect()