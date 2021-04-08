# ACSTutorial

The goal of this repository is to provide some very basic usage examples of the ACS framework. This repository contains several tutorials: each tutorial's folder contains:
* load_env.sh: a script that initialize the tutorial's environment. It creates the integration area (INTROOT) folder and initializes acs. 
* make_all.sh: a script to compile and install the tutorial's code.
* WORKSPACE: a folder that contains the components' code and the CDB configuration.
* README.md: a README explaining the tutorial.

## Tutorials summary

### Tutorial 1
**Goal**: development of a basic component.

**Implementation**: c++, python, java.

### Tutorial 2
**Goal**: development of two components "A" and "B": the component "A" calls a method of the "B" component. 

**Implementation**: c++, python, java.

### Tutorial 3
**Goal**: development of a component "Console" communicating with a component "Telescope" and with a "Database" **simulated** component.

**Implementation**: c++, xml.

### Tutorial 4
**Goal**: development of user-definied complex types. 

**Implementation**: c++, python, java.

### Tutorial 5
**Goal**: development of a component that can raise user-definied exceptions. Another component catches the exceptions.

**Implementation**: c++, python, java.

### Tutorial 6
**Goal**: compilation of an IDL module containing multiple interface definitions.

**Implementation**: no implementation.

### Tutorial 7
**Goal**: the README.md gives an overview of the different components types available in ACS

**Implementation**: no implementation.

### Tutorial 8
**Goal**: development of two components "Supplier" and "Consumer": the "Supplier" component communicates with the "Consumer" component using the ACS' notification channel.  

**Implementation**: python

### Tutorial 9
**Goal**: development of a custom Offshoot for reporting on asynchronous Call. 

**Implementation**: python



## How to start the tutorials

### How to start a tutorial using the ACS command center
1. In order to activate the ACS environemnt, call the "load_env" script inside the TUTORIAL_x folder with:
```bash
`source load_env.sh`
```
2. In order to compile and install the components' code, call the "make_all" script inside the TUTORIAL_x folder with:
```bash
`source make_all.sh`
```
3. The ACS Command Center GUI can be started with:
```bash
acscommandcenter
```
The ACS framework can be started clicking on the “Start” green button. 
4. The containers can be activated using the corresponding panel, writing the container's name and choosing its programming language (aragornContainer for python, bilboContainer for c++ and frodoContainer for java). 
5. In order to acquire a reference of a component and call its methods, you can use the object explorer tool: you can find it clicking on the “Tools” tab.


### How to start a tutorial using the terminal and ACS commands

DISCLAIMER: only TUTORIAL_9 has a "test" script.

1. In order to activate the ACS environemnt, call the "load_env" script inside the TUTORIAL_x folder with:
```bash
. load_env.sh
```
2. In order to compile and install the components' code, call the "make_all" script inside the TUTORIAL_x folder with:
```bash
`source make_all.sh`
```
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
 5. In order to acquire a component's reference to call its methods, you can use the ACS' PySimpleClient interface as shown [here](TUTORIAL_9/WORKSPACE/async_py_impl/test/testOnewayWithoutCallback.py)


