#include <HelloComponentImpl.h>
 
HelloComponentImpl::HelloComponentImpl(const ACE_CString& name, maci::ContainerServices * containerServices) : ACSComponentImpl(name, containerServices) {
}
 
HelloComponentImpl::~HelloComponentImpl() {
}
 
char* HelloComponentImpl::printHello() {
    std::cout << "Just printing 'Hello World!'" << std::endl;
    return CORBA::string_dup("Hello World!");
}
 
/* --------------- [ MACI DLL support functions ] -----------------*/
#include <maciACSComponentDefines.h>
MACI_DLL_SUPPORT_FUNCTIONS(HelloComponentImpl)
/* ----------------------------------------------------------------*/