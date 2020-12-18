package acsws.acstutorial.TelescopeImpl;

import alma.acs.component.ComponentImplBase;
import acsws.acstutorial.TelescopeOperations;

public class TelescopeImpl extends ComponentImplBase implements TelescopeOperations
{
    private float x;
    private float y;

    public TelescopeImpl()
    {
        this.x = 0;
        this.y = 0;
    }

    public void moveTo(float x, float y)
    {
        this.x = x;
        this.y = y;
    }

    public String getCurrentPosition()
    {   
        String position = "Telescope in x:" + this.x + " y:" + this.y;
        System.out.println(position);
        return position;
    }
}