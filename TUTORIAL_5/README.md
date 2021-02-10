# Tutorial 5
The goal of this tutorial is to develop a component that can raise user-defined exceptions. Another component will catch these exceptions. Based on Tutorial 2.

```bash
cd TUTORIAL_5
. load_env.sh
```
## IDL and XML Errors definition
Let's create the IDL interface for the Errors.
```bash
cd WORKSPACE
getTemplateForDirectory MODROOT_WS idlErrors
cd idlErrors
touch idl/ERRORS.idl
```
Each error is is definied with two numbers:
* ACSErr::ACSErrType -> namespace / IDL module
* ACSErr::ErrorCode -> exception class
Inside idl/ERRORS.idl a FOOErr and BARErr modules have been defined. Their types are 900907 and 900908 and they define a new ErrorCode (=0) associated with a user-defined exception "FooNotFound" and "BarNotFound". 

### XML Errors definition
In addition to the IDL interface, an xml description of the modules must be provided.
```bash
touch idl/FOOErr.xml
touch idl/BARErr.xml
```
The "name" attribute of the "Type" tag must be equal to the new module name (e.g. FOOErr) and the "type" attribute must be equal to the ACSErrType defined within the IDL (e.g. 900907). Then, each exception must be defined using the "ErrorCode" tag. 

### Compilation:
In order to compile the idl, you need to assign the name of the new module to the ACSERRDEF variable of the Makefile. 
**Makefile:**
```makefile
...
ACSERRDEF := FOOErr BARErr
```
```bash
cd src/
make clean all install
```
The compilation will generate FOOErr.idl and BARErr.idl from ERRORS.idl

## Telescope Component

### IDL definition file
Nothing new from TUTORIAL_2, except the "ERRORS.idl" is included and "moveTo" will raise an Exception.
```bash
    ...
    #include "FOOErr.idl"
    ...
    void moveTo(in float x, in float y)
    		raises (FOOErr::FooNotFoundEx);
    ...
```
In order to compile the idl, you need to link the library in which the errors are defined. This time **you don't specify the "STUBS" suffix**.

 **Makefile:**
```makefile
...
IDL_FILES = Telescope
TelescopeStubs_LIBS = acscomponent FOOErr
...
```
Then, as always:
```bash
cd src/
make clean all install
```
### C++ implementation:
The "TelescopeImpl.h" includes the "FOOErr.h" and the "TelescopeImpl.cpp" will raise the exception:
```cpp
throw FOOErr::FooNotFoundExImpl(__FILE__, __LINE__, "Telescope cannot move here!").getFooNotFoundEx();
```
Be careful here:
* FooNotFoundEx**Impl**: you need to specify the "Impl" suffix.
* **get**FooNotFoundEx: you need to use tht "get" prefix.

In order to compile the cpp implementation of the Telescope component, you need to link the library in which the errors are defined. This time **you don't specify the "STUBS" suffix**.

 **Makefile:**
```makefile
...
INCLUDES            = TelescopeImpl.h
...
LIBRARIES           = TelescopeImpl
TelescopeImpl_OBJECTS = TelescopeImpl
TelescopeImpl_LIBS    = TelescopeStubs acscomponent FOOErr maci
...
```
Then, as always:
```bash
cd src/
make clean all install
```

### JAVA implementation:
In order to throw FooNotFoundEx exception you need to import its wrapper located inside the jar file and call toNAME_EXCEPTION():


First you need to use the real exception to throw in the signature:

```java

import acsws.FOOErr.wrappers.AcsJFooNotFoundEx;
import acsws.FOOErr.FooNotFoundEx;

....

public void moveTo(float x, float y) throws FooNotFoundEx {

}

 ```
 Then you can throw the exception calling the wrapper:

 ```java

 throw new AcsJFooNotFoundEx("Error Message").toFooNotFoundEx();

```

**Makefile:**
```makefile
...
JARFILES = TelescopeImpl
TelescopeImpl_DIRS = acsws
...
```


## Console Component
### C++ implementation:
We want to make able the Console component to catch the Telescope's exception. 
* The IDL definition does not change
* The "ConsoleImpl.h" must include "BARErr.h"
* The "ConsoleImpl.cpp" can catch the exception using this syntax:
```cpp
try {
    telescope_component->moveTo(x, y);
}
catch(BARErr::BarNotFoundEx &_ex) { 
    std::cout << "====> Exception catched!!" << std::endl;
}
```
In order to compile the cpp implementation of the Console component, you need to link the library in which the errors are defined. This time **you don't specify the "STUBS" suffix**.

**Makefile:**
```makefile
...
INCLUDES            = ConsoleImpl.h
...
LIBRARIES           = ConsoleImpl
ConsoleImpl_OBJECTS = ConsoleImpl
ConsoleImpl_LIBS    = ConsoleStubs acscomponent BARErr TelescopeStubs maci
...
```
Then, as always:
```bash
cd src/
make clean all install
```

### JAVA implementation:
Handling FooNotFoundEx from telescope component is done simply using try catch statement, then for throwing a new exception you can use the previous instructions:
```java

import acsws.FOOErr.FooNotFoundEx;
import acsws.BARErr.wrappers.AcsJBarNotFoundEx;
import acsws.BARErr.BarNotFoundEx;
....

try {
    ....
}
catch (FooNotFoundEx ex)
{
    throw new AcsJBarNotFoundEx("Error Message").toBarNotFoundEx();

}

 ```

 **Makefile:**
```makefile
...
JARFILES = ConsoleImpl
TelescopeImpl_DIRS = acsws
...

