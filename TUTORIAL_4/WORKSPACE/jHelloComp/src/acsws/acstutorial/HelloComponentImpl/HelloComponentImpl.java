package acsws.acstutorial.HelloComponentImpl;
import alma.acs.component.ComponentImplBase;
import acsws.acstutorial.HelloComponentOperations;
import java.lang.Math;
import acsws.customtypes.Position;


public class HelloComponentImpl extends ComponentImplBase implements HelloComponentOperations {
    public HelloComponentImpl() {
    }
    
    
    public void printHi() 
    {
        System.out.println("Hello World!");
        m_logger.info("hello world!!");
    }

    public Position getPosition()
    {
        Position p = new Position(15.4, 12.4);
        m_logger.info("New position: " + p.az + ", " + p.el);
        return p;
        
    }

    public double computeDistance(Position p1, Position p2)
    {
        double distance = 0;
        distance = Math.sqrt(Math.pow((p2.az - p1.az), 2) + Math.pow((p2.el - p1.el), 2));

        return distance;
    }

    public double computeCenterOfMass()
    {
        return 42;
    }

}