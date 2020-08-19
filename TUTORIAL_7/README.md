# Tutorial 7
The goal of this tutorial is to explore the different components' types. Only Python implementations.
```bash
cd TUTORIAL_7
. load_env.sh
```
The Components' types:
* Component
* Default Component
* Non-Sticky Component
* Collocated Component
* Dynamic Component
* AutoStart Component
* Immortal Component
* Delayed Deactivation Component

All this Components are ACS Components or ACS CharacteristicComponents: the main difference is how they are configured and started by the client.

## Normal Component
Regular component
```xml
<e Name="CLOCK1"
   Code="acsclock"
   Type="IDL:alma/acstime/Clock:1.0"
   Container="bilboContainer"
   ImplLang="cpp"/>
```

## Default Component
Rules:
* Must be just one default component for each IDL Interface in Components.xml
* Client must request component type (`IDL:acsws/acstutorial/DefaultComponent:1.0`) instead of the component name

```xml
<e Name="PY_DEFAULT_COMP"
    Code="DEFAULTCOMP.DefaultComponentImpl"
    Type="IDL:acsws/acstutorial/DefaultComponent:1.0"
    Container="aragornContainer"
    ImplLang="py"
    Default="true"/>
```

## Non-Sticky Component
When you ask for a weak reference (non-sticky), if the Component has not been created yet, you cant get the reference. If the Component has already been created and you request for a non-sticky reference, you get the reference but the references counter will not be increased. 

This behaviour is shown by the acscommand center when you try to get a reference to a Component through the Object Explorer Tool: 
```
Connection to Component 'COMP_NAME' failed. Connect as non-sticky mode is enabled: in this mode Component will not be activated by the Object Explorer, only already activated component will be accessed. 
```
And then, it asks you if you want to get a "sticky-reference" for the Component. If instead you acquire a reference (activate) to the Component, through the acscommandcenter first, then the Object Explorer will give you the non-sticky reference. 

If you want to get a weak reference using the ACS api you can use the getComponentNonSticky() method of the Container Service.

## Collocated Component
This features is supported only for C++. If you call a Component's method, youl will pass through several CORBA layers before reaching the actual implementation. If the client is in the same container of the Component, you can avoid those layers and call directly the Component's method implementation. The call performance is improved. The Container Service has a method call getCollocatedComponent() and you pass the reference you want to get. 

```python
from Acspy.Clients.SimpleClient import PySimpleClient
import maci
 
client = PySimpleClient()
compSpec = maci.ComponentSpec("PY_HELLO_COMP", "*", "*", "*")
comp = client.getCollocatedComp(compSpec, False, "PY_HELLO_COMP")
```

## Dynamic Component
It is a regular component that can be created a run time. You can create an arbitrary number of dynamic components, but you need to choose the component's Name. In ALMA this is used for the array creation, all the logical units are dynamic. In Python you can decide at run time also the container in which the Component will be created.

```xml
<e Name="*"
   Code="DEFAULTCOMP.DefaultComponentImpl"
   Type="IDL:acsws/acstutorial/DefaultComponent:1.0"
   Container="aragornContainer"
   ImplLang="py">
</e>
```
## AutoStart Component
This is a Component that starts at the moment the container starts. When the container connects to the Manager, the Manager will instantiate a reference to the Component.
```xml
<e Name="PY_DEFAULT_COMP"
    Code="DEFAULTCOMP.DefaultComponentImpl"
    Type="IDL:acsws/acstutorial/DefaultComponent:1.0"
    Container="aragornContainer"
    ImplLang="py"
    Autostart="true"/>
```

## Immortal Component
The Component will never get destroyed (even if the references counter reachs zero). 
```xml
<e Name="PY_DEFAULT_COMP"
    Code="DEFAULTCOMP.DefaultComponentImpl"
    Type="IDL:acsws/acstutorial/DefaultComponent:1.0"
    Container="aragornContainer"
    ImplLang="py"
    KeepAliveTime="-1"/>
```

## Delayed Deactivation Component
The KeepAliveTime specify the number of seconds after the Component is destroyed when the references counter reaches zero. It is not very used in ALMA.
```xml
<e Name="PY_DEFAULT_COMP"
    Code="DEFAULTCOMP.DefaultComponentImpl"
    Type="IDL:acsws/acstutorial/DefaultComponent:1.0"
    Container="aragornContainer"
    ImplLang="py"
    KeepAliveTime="10"/>
```
