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
1. load the ACS environment and set the needed environment variable
2. compile the components' code: the instruction are written inside the TUTORIAL_x's README
3. start the ACS framework    
4. start the ACS containers
5. acquire a reference of the desidered component and call its methods

### Starting the tutorial using the ACS command center (reccomended way)
1. In order to activate the ACS environemnt, call the "load_env" script inside the TUTORIAL_x folder with:
```bash
`. load_env.sh`
```
2. The components' code must be compiled and installed: the instructions are written inside the TUTORIAL_x's README.

3. The ACS Command Center GUI can be started with:
```bash
acscommandcenter
```
The ACS framework can be started clicking on the “Start” green button. 
4. The containers can be activated using the corresponding panel, writing the container's name and choosing its programming language. 
5. In order to acquire a reference of a component and call its methods, you can use the object explorer tool: you can find it clicking on the “Tools” tab.


### Starting the tutorial using the terminal and ACS commands
1. In order to activate the ACS environemnt, call the "load_env" script inside the TUTORIAL_x folder with:
```bash
. load_env.sh
```
2. The components' code must be compiled and installed: the instructions are written inside the TUTORIAL_x's README. 

3. The ACS framework can be started with:
```bash
acsStart
```
4. Once ACS framework is up and running, the containers can be started. There are 3 default containers inside the ACS framework, one for each supported language. They can be started with (each one in a seprate terminal):
```bash
acsStartContainer -cpp bilboContainer
acsStartContainer -java frodoContainer
acsStartContainer -py aragornContainer
```
 5. In order to acquire a reference of a component and call its methods, you can:
 * call the python script inside the test/ folder:
 ```bash
 cd TUTORIAL_x
 python test/client.py
 ```
 * **OR** start the *object explorer tool* with:
 ```bash
 objexp
 ```


