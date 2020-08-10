#include <HelloComponentImpl.h>
 
HelloComponentImpl::HelloComponentImpl(const ACE_CString& name, maci::ContainerServices * containerServices) : ACSComponentImpl(name, containerServices) {
}
 
HelloComponentImpl::~HelloComponentImpl() {
}
void HelloComponentImpl::printHi() {
    return;
}

 
::CORBA::Double HelloComponentImpl::computeDistance(const customtypes::Position& p1, const customtypes::Position& p2) {
    return ::CORBA::Double(10);
}
::CORBA::Double HelloComponentImpl::computeCenterOfMass(/*customtypes::Contour c*/) {
    return ::CORBA::Double(10);
}


 
/* --------------- [ MACI DLL support functions ] -----------------*/
#include <maciACSComponentDefines.h>
MACI_DLL_SUPPORT_FUNCTIONS(HelloComponentImpl)
/* ----------------------------------------------------------------*/