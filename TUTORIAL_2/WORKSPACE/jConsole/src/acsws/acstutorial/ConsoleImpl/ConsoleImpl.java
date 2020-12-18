package acsws.acstutorial.ConsoleImpl;

import alma.acs.component.ComponentImplBase;
import acsws.acstutorial.ConsoleOperations;
import alma.JavaContainerError.wrappers.AcsJContainerServicesEx;
import acsws.acstutorial.Telescope;
import acsws.acstutorial.TelescopeHelper;

public class ConsoleImpl extends ComponentImplBase implements ConsoleOperations
{
    
    public ConsoleImpl()
    {}

    public void setTelescopePosition(float x, float y)
    {
        Telescope telescope = null;
        try 
        {
            telescope = TelescopeHelper.narrow(this.m_containerServices.getComponent("J_TELESCOPE"));
        } catch (AcsJContainerServicesEx ex) 
        {
            m_logger.severe("J_TELESCOPE component not found");
            throw new RuntimeException(ex);
        }
        
        
        telescope.moveTo(x, y);

        m_containerServices.releaseComponent(telescope.name());
    }
    
    public String getTelescopePosition()
    {
        Telescope telescope = null;
        try {
            telescope = TelescopeHelper.narrow(this.m_containerServices.getComponent("J_TELESCOPE"));
        } catch (AcsJContainerServicesEx ex) {
            m_logger.severe("J_TELESCOPE component not found");
            throw new RuntimeException(ex);
        }

        String s = telescope.getCurrentPosition();

        System.out.println(s);

        m_containerServices.releaseComponent(telescope.name());

        return s;
    }


}
