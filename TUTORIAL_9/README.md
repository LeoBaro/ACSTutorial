# Tutorial 9
The goal of this tutorial is to develop of a custom Offshoot for reporting on asynchronous calls. 

Languages:
* Python

```bash
cd TUTORIAL_9
source load_env.sh
source make_all.sh
```

## Asynchronous methods
*The most common use of communication in ACS is the use of synchronous calls, however there are different reasons why someone could be interested in a different kind of calls. For this, CORBA provides the definition of 'oneway' methods, which basically are dispatched and no response is expected by the client.*

First of all, let's try out a 'oneway' method.
* The AsyncModule (defined [here](WORKSPACE/async/idl/AsyncModule.idl)) contains the AsyncExample interface that defines a 'oneway' method called: delayResultWithOutCallback(..). 
* In order to use the 'oneway' keyword, you need to include <acscommon.idl> and link the acscommonStubs lib in the [Makefile](WORKSPACE/async/src/Makefile)
* The python implementation is straightforward, you can find it within the AsyncExampleImpl class, defined [here](WORKSPACE/async_py_impl/src/ASYNC_IMPL_MODULE/AsyncExampleImpl.py).  
* You can try it out calling [this script](WORKSPACE/async_py_impl/test/testOnewayWithoutCallback.py) (you need to start acs first and also start the corresponding containers (defined [here](WORKSPACE/CDB/Components/Components.xml)))


## Reporting on asynchronous methods
ACS adds callbacks functionality with two types of classes:
* Offshoots are the most basic form to report back to the caller. The base interface is actually empty, allowing anyone to extend such interface as they prefer.
* Callbacks are in fact a specialization of the Offshoot and were designed to be used mainly by BACI (Monitoring, Actions, etc.). ACS provides some Callbacks for basic types:
  * CBvoid
  * CBdouble(Seq)
  * CBfloat(Seq)
  * CBstring(Seq)
  * CBlong(Seq)
  * CBuLong(Seq)
  * CBboolean(Seq)
  * CBlongLong
  * CBuLongLong

**IMPORTANT**: those mechanisms are not based on pure (javascript-style) callback functions. Instead, ACS OffShoots and ACS Callbacks are objects that are passed by the client to the server, so that the server can later invoke methods on the callback and thus inform the client of a change in status, completion of some operation, and the like. 


## Reporting on asynchronous methods with OffShoots
Since the OffShoot base interface is actually empty, we need to implement it. 
* The AsyncModule (defined [here](WORKSPACE/async/idl/AsyncModule.idl)) defines an interface called MyCallback, that implements ACS::OffShoot. 
* The MyCallback interface can define any methods you like. 
* You can find [here](WORKSPACE/callback_py_impl/src/CALLBACKS_IMPL_MODULE/MyCallbackImpl.py) the implementation of the MyCallback interface: the MyCallBack object mantains a state composed by a *status* field (that is changed by the constructor, the working() and the done() methods ) and a *data* value (that is used for communication purposes between async call invocations). The get() method of the interface returns a tuple containing the status and the data fields. 

Now we need to create a 'oneway' method that accepts a callback as an input argument.
* The AsyncModule (defined [here](WORKSPACE/async/idl/AsyncModule.idl)) contains the AsyncExample interface that defines a 'oneway' method called: delayResultWithCallback(..). 
* As before, you can find the python implementation within the AsyncExampleImpl class, defined [here](WORKSPACE/async_py_impl/src/ASYNC_IMPL_MODULE/AsyncExampleImpl.py).
* You can try it out calling [this script](WORKSPACE/async_py_impl/test/testOnewayWithCallback.py) (you need to start acs first and also start the corresponding containers (defined [here](WORKSPACE/CDB/Components/Components.xml))).


## Issue to be aware of

Python oneway methods are not working when both the caller and callee are on the same container.

See [ticket](https://ictjira.alma.cl/browse/ACS-6).

* You can try it out calling [this script](WORKSPACE/async_py_impl/test/testOnewayWithCallbackFromComponent.py) (you need to start acs first and also start the corresponding containers (defined [here](WORKSPACE/CDB/Components/Components.xml)))



## Additional documentation: 
* https://confluence.alma.cl/display/ICTACS/ACS+Workshop+-+Asynchronous+Calls#ACSWorkshop-AsynchronousCalls-Python
* https://confluence.alma.cl/display/ICTACS/2020/11/10/Asynchronous+Calls#AsynchronousCalls-Offshoots