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

    try {
        telescope_component->moveTo(x, y);
    }
    catch(FOOErr::FooNotFoundEx &_ex) { 
        std::cout << "====> Exception catched!!" << std::endl;
        throw BARErr::BarNotFoundExImpl(__FILE__, __LINE__, "moveTo(..) raises an Exception: x < 0").getBarNotFoundEx();

    }

    this->getContainerServices()->releaseComponent(telescope_component->name());

    return;
}  

 
/* --------------- [ MACI DLL support functions ] -----------------*/
#include <maciACSComponentDefines.h>
MACI_DLL_SUPPORT_FUNCTIONS(ConsoleImpl)
/* ----------------------------------------------------------------*/