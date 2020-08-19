from Acspy.Clients.SimpleClient import PySimpleClient
 
client = PySimpleClient()
 
hc_py = client.getComponent("PY_HELLO_COMP")
hc_cpp = client.getComponent("CPP_HELLO_COMP")
 
print(hc_py.printHello())
print(hc_cpp.printHello())