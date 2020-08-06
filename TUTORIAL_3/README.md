# Tutorial 3
The goal of this tutorial is to have a component "Console" communicating with a component "Telescope" and with a "Database" **simulated** component. The CDB Simulated Components are a quick way to make a component available for development and testing. They could be used to prototype basic functionality and to mock-up components in order to prepare module tests which need to interact with other components.
```bash
cd TUTORIAL_3
. load_env.sh
```
In order to setup a Telescope and a Console component, follow the TUTORIAL_2's README.

## IDL Database Simulated Component
Let's create the IDL interface for the simulated Database.
```bash
cd WORKSPACE
getTemplateForDirectory MODROOT_WS idlSimDatabase
cd idlSimDatabase
touch idl/SimDatabase.idl
```
This component will simulate a "store proposal" functionality and "count stored proposals" functionalty, something like:
```sql
INSERT INTO Proposals(pid, ez, el, expTime) VALUES(1, 10, 30, 5);
SELECT COUNT(*) FROM Proposals;
```
**Makefile:**
```makefile
...
IDL_FILES = SimDatabase
SimDatabaseStubs_LIBS = acscomponentStubs
...
COMPONENT_HELPERS=on
```
Nothing new from the previous tutorial.
**Compilation:**
```bash
cd src/
make clean all install
```
### Simulated Database implementation
The simulation code needs to be put in the CDB:
```bash
mkdir -p CDB/alma/simulated/SIM_DATABASE
touch CDB/alma/simulated/SIM_DATABASE/SIM_DATABASE.xml
```
The 'setGlobalData' and 'getGlobalData' can be used store some values to be shared (or used) in other methods and it works also for internal state. 

The simulated component must be added within the CDB components configuration:

**CDB/MACI/Components/Components.xml**
```xml
   <e Name="SIM_DATABASE" Code="Acssim.Servants.Simulator"
      Type="IDL:acsws/acstutorial/SimDatabase:1.0"
      Container="aragornContainer"
      ImplLang="py"/>
```

## Console Component
A method has been added to the Console component in order to interact with the simulated database (check idl/Console.idl).
### C++ implementation
**Makefile:**
```makefile
...
INCLUDES            = ConsoleImpl.h
LIBRARIES           = ConsoleImpl
ConsoleImpl_OBJECTS = ConsoleImpl
ConsoleImpl_LIBS    = ConsoleStubs acscomponent TelescopeStubs SimDatabaseStubs maci
...
```
Since we are including the SimDatabase client implementation we need to link the corresponding library. In addition, since we call the "getContainerServices()" and "getComponent()" methods we need to link the "libmaci".

**Compilation:**
```bash
cd src/
make clean all install
```
### Python implementation [TODO]
```bash
cd WORKSPACE
getTemplateForDirectory MODROOT_WS pyConsole
cd pyConsole
mkdir src/acstut
touch src/acstut/__init__.py
touch src/acstut/ConsoleImpl.py
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