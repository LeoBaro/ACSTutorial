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

### Tutorial 2
Goal: create two custom components A and B: the first component A calls a method of the B component. C++ and Python implementations.


## How to start the tutorials
In order to test TUTORIAL_x's components, you need to:
* load the ACS environment and set the needed environment variable
* compile the components' code: the instruction are written inside the TUTORIAL_x's README
* start the ACS framework    
* start the ACS containers
* acquire a reference of the desidered component and call its methods

### Starting the tutorial using the ACS command center (reccomended way)
In order to activate the ACS environemnt, call the "load_env" script inside the TUTORIAL_x folder with:
```bash
`. load_env.sh`
```
Then you have to compile the components' code: the instruction are written inside the TUTORIAL_x's README.
The ACS Command Center GUI can be started with:
```bash
acscommandcenter
```
The ACS framework can be started clicking on the “Start” green button. The containers can be activated using the corresponding panel, writing the container's name and choosing its programming language. In order to acquire a reference of a component and to call its methods, you can use the object explorer tool: you can find it clicking on the “Tools” tab.


### Starting the tutorial using the ACS command center (reccomended way)
In order to activate the ACS environemnt, call the "load_env" script inside the TUTORIAL_x folder with:
```bash
`. load_env.sh`
```
Then you have to compile the components' code: the instruction are written inside the TUTORIAL_x's README. The ACS framework can be started with:
```bash
acsStart
```
Once ACS framework is up and running, the containers can be started. There are 3 default containers inside the ACS framework, one for each supported language. They can be started with (each one in a seprate terminal):
```bash
acsStartContainer -cpp bilboContainer
acsStartContainer -java frodoContainer
acsStartContainer -py aragornContainer
```
 In order to acquire a reference of a component and to call its methods, you can:
 * call the python script inside the test/ folder:
 ```bash
 cd TUTORIAL_x
 python test/client.py
 ```
 * start the *object explorer tool* with:
 ```bash
 objexp
 ```


