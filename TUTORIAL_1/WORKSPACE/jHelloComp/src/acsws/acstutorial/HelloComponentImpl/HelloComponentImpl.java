//Suggested: import alma.<Module>.<Interface>Impl; //But anything, really
package acsws.acstutorial.HelloComponentImpl;
  
//Base component implementation, including container services and component lifecycle infrastructure
import alma.acs.component.ComponentImplBase;
  
//Skeleton interface for server implementation
import acsws.acstutorial.HelloComponentOperations;
 
 
//ClassName usually is <Interface>Impl, but can be anything
public class HelloComponentImpl extends ComponentImplBase implements HelloComponentOperations {
    public HelloComponentImpl() {
    }
    public String printHello() {
        System.out.println("Hello World!");
        return new String("Hello World!");
    }
}
