package acsws.acstutorial.TelescopeImpl;

import alma.acs.component.ComponentImplBase;
import acsws.acstutorial.TelescopeOperations;
import acsws.FOOErr.wrappers.AcsJFooNotFoundEx;
import acsws.FOOErr.FooNotFoundEx;

public class TelescopeImpl extends ComponentImplBase implements TelescopeOperations {
    private float x;
    private float y;

    public TelescopeImpl() {

        this.x = 0;
        this.y = 0;
    }

    @Override
    public void moveTo(float x, float y) throws FooNotFoundEx{

        if (x < 0 || y < 0)
        {   
            m_logger.severe("ERROR: Positions must be greater than zero");
            throw new AcsJFooNotFoundEx("ERROR Positions must be greater than zero").toFooNotFoundEx();
        }

        this.x = x;
        this.y = y;
    }

    public String getCurrentPosition() {
        String position = "Telescope in x:" + this.x + " y:" + this.y;
        System.out.println(position);
        return position;
    }
}