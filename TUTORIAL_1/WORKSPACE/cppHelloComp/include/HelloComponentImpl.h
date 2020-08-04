#ifndef _HELLO_COMPONENT_IMPL_H
#define _HELLO_COMPONENT_IMPL_H
 
#ifndef __cplusplus
#error This is a C++ include file and cannot be used from plain C
#endif
 
//Base component implementation, including container services and component lifecycle infrastructure
#include <acscomponentImpl.h>
 
//Skeleton interface for server implementation
#include <HelloComponentS.h>
 
//Error definitions for catching and raising exceptions
class HelloComponentImpl : public virtual acscomponent::ACSComponentImpl, public virtual POA_workshop::HelloComponent {
  public:
    HelloComponentImpl(const ACE_CString& name, maci::ContainerServices * containerServices);
    virtual ~HelloComponentImpl();
    char* printHello();
};
 
#endif