# Tutorial 1

```bash
cd TUTORIAL_1
. load_env.sh
cd WORKSPACE
```
## IDL Component
```bash
getTemplateForDirectory MODROOT_WS idlHelloComp
cd idlHelloComp
touch idl/HelloComponent.idl
```
Makefile:
```makefile
...
IDL_FILES = HelloComponent
HelloComponentStubs_LIBS = acscomponentStubs
...
COMPONENT_HELPERS=on
```
Compilation:
```bash
cd src/
make clean all install
```
## C++ implementation
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

