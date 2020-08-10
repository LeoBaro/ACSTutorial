#ifndef _CONSOLE_IMPL_H
#define _CONSOLE_IMPL_H
 
#ifndef __cplusplus
#error This is a C++ include file and cannot be used from plain C
#endif
 
//Base component implementation, including container services and component lifecycle infrastructure
#include <acscomponentImpl.h>
 
//Skeleton interface for server implementation
#include <ConsoleS.h>
 
//Interface of clients for connection
#include <TelescopeC.h>

//Error definitions for catching and raising exceptions
class ConsoleImpl : public virtual acscomponent::ACSComponentImpl, public virtual POA_acstutorial::Console {
  public:
    ConsoleImpl(const ACE_CString& name, maci::ContainerServices * containerServices);
    virtual ~ConsoleImpl();
    char* getTelescopePosition();
    void setTelescopePosition(float x, float y);    
};
 
#endif
