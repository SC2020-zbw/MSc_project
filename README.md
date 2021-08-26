# MSc project

## Integrating Jupyter with UCL HPC systems

 *  Users need to have Myriad account
 *  Users need to have Jupyter in local laptop

## Usage

### Perparing Jupyter notebook linking to Myriad

 * For users inside the UCL firewall, create a local host and log in Myriad account with UCL username and password, **uccaxxx** is your seven-character username.
```shell
ssh -L 8081:localhost:8081 uccaxxx@myriad.rc.ucl.ac.uk
```
 * For users outside the UCL firewall, create a local host and log in Myriad account with UCL username and password, **uccaxxx** is your seven-character username.
```shell
ssh -L 8081:localhost:8081 -o ProxyJump=uccaxxx@socrates.ucl.ac.uk uccaxxx@myriad.rc.ucl.ac.uk
```
 * Git clone the repository
```shell
git clone git@github.com:SC2020-zbw/MSc_project.git
```
```shell
cd MSc_project
```
 * load python3 module
```shell
module load python3/recommended
```
 * open the jupyter notebook.
```shell
virtualenv jupyter
```
```shell
source jupyter/bin/activate
```
```shell
pip3 install jupyter
```
```shell
jupyter notebook --port=8081
```
 * Copy the URL and open it in local browser
 

 ## Examples

There are two examples in the folder **examples**. Mandelbrot and LAMPPS

### Mandelbrot

 ```python

 ```

The python file to generate Mandelbrot set and to plot the figure are created without using library, the rest of work is to generate the scripts then submit the job in **Myriad** and finally check the output as well as returning figure.
