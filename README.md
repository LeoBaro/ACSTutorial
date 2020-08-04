# ACSTutorial

The goal of this repository is to provide some usage examples of the ACS framework. This repository contains several tutorials, each tutorial is inside the corresponding folder. Inside each folder there are the following elements:

* load_env.sh: a script that initialize the environment. It creates an integration area (INTROOT) folder and set the needed environment variables.
* WORKSPACE: a folder that contains the components and a custom CDB configuration.
* README.md: a README that describes how to integrate the components inside the ACS framework.

## Installation
Clone this repository in the $HOME folder (/home/almamgr) of the ACS virtual machine.

## Tutorials 

### Tutorial 1
Goal: create a custom simple component. C++ and Python implementations.

### Tutorial 2 (work in progress)
Goal: create a more complex custom component with a method with an input and output parameters with custom types. C++ and Python implementations.


## How to start the ACS framework

In order to use the ACS system, its services and containers need to be started. There are two ways of doing that:
* using the ACS commands from the terminal
* starting the Command Center GUI
In both cases the ACS environment must be loaded: you can do it using the *load_env.sh* script inside each TUTORIAL folder.

### Using the terminal
The command to start the services is the following:
```bash
acsStart
```
Once the services are up and running, the containers can be started. There are 3 default containers inside the ACS framework, one for each supported language. They can be started with:
```bash
acsStartContainer -cpp bilboContainer
acsStartContainer -java frodoContainer
acsStartContainer -py aragornContainer
```
There are also two useful tools, the **object explorer tool** that allows to interact with the components, calling their methods or inspecting their state, and the **logger tool** that can be used to inspect the logging messages dumped by the framework.
```bash
objexp
jlog
```

### Using the Command Center GUI
The GUI can be started with:
```bash
acscommandcenter
```
The services can be started clicking on the “Start” green button. The containers can be activated using the corresponding panel. The object explorer and logger tools can be activated clicking on the “Tools” tab.