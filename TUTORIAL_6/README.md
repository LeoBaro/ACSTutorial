# Tutorial 6
The goal of this tutorial is to compile an IDL file containing multiple interface definitions.
```bash
cd TUTORIAL_6
. load_env.sh
```
## IDL Component
Let's create the component interface:
```bash
cd WORKSPACE
getTemplateForDirectory MODROOT_WS idlGenericModule
cd idlGenericModule
touch idl/GenericModule.idl
```
**idl/GenericModule.idl:**
```cpp
#ifndef _GENERIC_MODULE_IDL_
#define _GENERIC_MODULE_IDL_
 
#pragma prefix "acsws"
 
#include <acscomponent.idl>
 
module acstutorial {
    interface FooComponent : ACS::ACSComponent {
        string sayHi();
    };
    interface BarComponent : ACS::ACSComponent {
        string sayHello();
    };
};
 
#endif
```
**Makefile:**
```makefile
...
IDL_FILES = GenericModule
FooComponentStubs_LIBS = acscomponentStubs
BarComponentStubs_LIBS = acscomponentStubs
...
COMPONENT_HELPERS=on
```
**Compilation:**
```bash
cd src/
make clean all install
```