#include <ConsoleImpl.h>
 
ConsoleImpl::ConsoleImpl(const ACE_CString& name, maci::ContainerServices * containerServices) : ACSComponentImpl(name, containerServices) {
}
 
ConsoleImpl::~ConsoleImpl() {
}
 
char* ConsoleImpl::getTelescopePosition() {

    acstutorial::Telescope_var telescope_component = this->getContainerServices()->getComponent<acstutorial::Telescope>("CPP_TELESCOPE");

    char* tel_pos = telescope_component->getCurrentPosition();

    this->getContainerServices()->releaseComponent(telescope_component->name());

    return CORBA::string_dup(tel_pos);
}

void ConsoleImpl::setTelescopePosition(float x, float y) {
    
    acstutorial::Telescope_var telescope_component = this->getContainerServices()->getComponent<acstutorial::Telescope>("CPP_TELESCOPE");

    telescope_component->moveTo(x, y);

    this->getContainerServices()->releaseComponent(telescope_component->name());

    return;
}  

 
bool ConsoleImpl::insertProposalInDatabase(int pid, double ez, double el, int expTime) {

    acstutorial::SimDatabase_var database_component = this->getContainerServices()->getComponent<acstutorial::SimDatabase>("SIM_DATABASE");

    bool result = database_component->storeProposal(pid, ez, el, expTime);

    this->getContainerServices()->releaseComponent(database_component->name());

    return result;
}


/* --------------- [ MACI DLL support functions ] -----------------*/
#include <maciACSComponentDefines.h>
MACI_DLL_SUPPORT_FUNCTIONS(ConsoleImpl)
/* ----------------------------------------------------------------*/