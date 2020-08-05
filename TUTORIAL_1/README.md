# Tutorial 1
The goal of this tutorial is to create a custom simple component.
```bash
cd TUTORIAL_1
. load_env.sh
```
## IDL Component
Let's create the component interface:
```bash
cd WORKSPACE
getTemplateForDirectory MODROOT_WS idlHelloComp
cd idlHelloComp
touch idl/HelloComponent.idl
```
**idl/HelloComponent.idl:**
```cpp
#ifndef _HELLOCOMPONENT_IDL_
#define _HELLOCOMPONENT_IDL_
 
#pragma prefix "acsws"
 
#include <acscomponent.idl>
 
module acstutorial {
    interface HelloComponent : ACS::ACSComponent {
        string printHello();
    };
};
 
#endif
```
Let's explain how the IDL code is translated into the supported languages.
* "acsws" is explained [in the official documentation](https://confluence.alma.cl/pages/viewpage.action?pageId=54002637).
* "acstutorial" will be a namespace in c++ and a package in python.
* "HelloComponent" will be the interface class that inherits from the "ACSComponent" class.

**Makefile:**
```makefile
...
IDL_FILES = HelloComponent
HelloComponentStubs_LIBS = acscomponentStubs
...
COMPONENT_HELPERS=on
```
Let's explain the Makefile variables:
* "IDL_FILES": all the IDL files listed here will be compiled.
* "HelloComponentStubs_LIBS": we need to create this variable that is used to specify which library will be linked to our component's stubs (client) code. The "acscomponentStubs" library is linked.
* "COMPONENT_HELPERS": Java Component Helper Classes generation on/off

**Compilation:**
```bash
cd src/
make clean all install
```
The compilation step of the IDL will generate "stub" code (client-side code) and "skeleton" code (server-side code). In particular, the following files are generated:
* C++
    * object/HelloComponentS.h ==> "S" for server
    * object/HelloComponentS.cpp
    * object/HelloComponentC.h ⇒ "C" for client: it contains the interface class we need to implement
    * object/HelloComponentC.cpp
    * lib/HelloComponentStubs.a
    * lib/HelloComponentStubs.so
* Python
    * Una cartella (pacchetto python) / site-packages / 
        * <idl-module-name> folder
        * HelloComponent_idl.py
        * <idl-module-name>__POA folder
* Java
    * lib/HelloComponent.jar
    * Folder HelloComponent/
        * Helper classes
        * src/<pragma-prefix>/<idl-module-name>/HelloComponentImpl/HelloComponentHelper.java.tpl

The installation step will move the files within the integration area folder that is pointed by $INTROOT.

## C++ implementation
We must now create a class to implement the interface.
```bash
getTemplateForDirectory MODROOT_WS cppHelloComp
cd cppHelloComp
touch include/HelloComponentImpl.h
touch src/HelloComponentImpl.cpp
```
Makefile:
```makefile
...
INCLUDES        = HelloComponentImpl.h
LIBRARIES = HelloComponentImpl
HelloComponentImpl_OBJECTS = HelloComponentImpl
HelloComponentImpl_LIBS = HelloComponentStubs acscomponent
...
```
Compilation:
```bash
cd src/
make clean all install
```
## Python implementation
```bash
getTemplateForDirectory MODROOT_WS pyHelloComp
cd pyHelloComp
mkdir src/acstut
touch src/acstut/__init__.py
touch src/acstut/HelloComponentImpl.py
```
Makefile:
```makefile
...
PY_PACKAGES        = acstut
...
```
Compilation:
```bash
cd src/
make clean all install
```
## MACI
CDB/MACI/Components/Components.xml
```xml
  <e Name="CPP_HELLO_COMP"
     Code="HelloComponentImpl"
     Type="IDL:acsws/acstutorial/HelloComponent:1.0"
     Container="bilboContainer"
     ImplLang="cpp"/>

  <e Name="PY_HELLO_COMP"
     Code="acstut.HelloComponentImpl"
     Type="IDL:acsws/acstutorial/HelloComponent:1.0"
     Container="aragornContainer"
     ImplLang="py"/>
```

