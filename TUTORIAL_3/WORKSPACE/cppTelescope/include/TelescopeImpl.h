#ifndef _TELESCOPE_IMPL_H
#define _TELESCOPE_IMPL_H
 
#ifndef __cplusplus
#error This is a C++ include file and cannot be used from plain C
#endif
 
//Base component implementation, including container services and component lifecycle infrastructure
#include <acscomponentImpl.h>
 
//Skeleton interface for server implementation
#include <TelescopeS.h>

// float -> string conversion utility
#include <sstream>
 
//Error definitions for catching and raising exceptions
class TelescopeImpl : public virtual acscomponent::ACSComponentImpl, public virtual POA_acstutorial::Telescope {
  public:
    TelescopeImpl(const ACE_CString& name, maci::ContainerServices * containerServices);
    virtual ~TelescopeImpl();
    void moveTo(float x, float y);
    char* getCurrentPosition();

  private:
    float x_pos;
    float y_pos;
};
 
#endif
