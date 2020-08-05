#include <ConsoleImpl.h>
 
ConsoleImpl::ConsoleImpl(const ACE_CString& name, maci::ContainerServices * containerServices) : ACSComponentImpl(name, containerServices) {
}
 
ConsoleImpl::~ConsoleImpl() {
}
 
bool ConsoleImpl::isTelescopePointing() {

    acstutorial::Telescope_var telescope_component = this->getContainerServices()->getComponent<acstutorial::Telescope>("CPP_TELESCOPE");

    bool p_status = telescope_component->getPointingStatus();

    this->getContainerServices()->releaseComponent(telescope_component->name());

    return p_status;
}

void ConsoleImpl::setTelescopePosition(float x, float y) {
    
    acstutorial::Telescope_var telescope_component = this->getContainerServices()->getComponent<acstutorial::Telescope>("CPP_TELESCOPE");

    telescope_component->setPosition(x, y);

    this->getContainerServices()->releaseComponent(telescope_component->name());

    return;
}  

 
/* --------------- [ MACI DLL support functions ] -----------------*/
#include <maciACSComponentDefines.h>
MACI_DLL_SUPPORT_FUNCTIONS(ConsoleImpl)
/* ----------------------------------------------------------------*/