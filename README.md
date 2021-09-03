# MSc project

## Integrating Jupyter with UCL HPC systems

The goal of project is to use Jupyter notebook as the frontend of Myriad instead of Bash. A python library is written and two examples in jupyter notebook are used to show how library works.

There are two prerequistes
 *  Users need to have Myriad account
 *  Users need to have Jupyter in local laptop

## Usage

### Open Jupyter notebook linking to Myriad
 * Open the terminal
 * For users inside the UCL firewall, link to Myriad account with UCL username and password, **uccaxxx** is your seven-character username.
```command
ssh -L 8081:localhost:8081 uccaxxx@myriad.rc.ucl.ac.uk
```
 * For users outside the UCL firewall, link to Myriad account with UCL username and password, **uccaxxx** is your seven-character username.
```command
ssh -L 8081:localhost:8081 -o ProxyJump=uccaxxx@socrates.ucl.ac.uk uccaxxx@myriad.rc.ucl.ac.uk
```
 * Git clone the repository
```command
git clone https://github.com/SC2020-zbw/MSc_project.git
```
 * Change directory to MSc_project
```command
cd MSc_project
```
 * load python3 module
```command
module load python3/recommended
```
 * open the jupyter notebook. 
```command
virtualenv jupyter
```
```command
source jupyter/bin/activate
```
```command
pip3 install jupyter
```
```command
jupyter notebook --no-browser --ip=127.0.0.1 --port=8081
```
 * Copy the URL and open it in local browser

After the first time succeed in installing the jupyter, two terminal commands **virtualenv jupyter** and **pip3 install jupyter** are not necessary to open the jupyter notebook. 
For **virtualenv jupyter**, Since there is no jupyter at first, an virtual environment is necessary at first. Then after **pip3 install jupyter**, Jupyter is then installed.

### Run examples

There are two examples in the folder **examples**, Mandelbrot and LAMPPS. There are two screenshots for these two examples when examples running successfully.

#### Mandelbrot

The python file **mandelbrot.py** is used to generate Mandelbrot set and to plot the figure, the rest of work is to generate the scripts then submit the job in **Myriad** and finally check the output as well as returning figure.

#### LAMMPS

**in.rhodo.scaled** and **data.rhodo** are necessary files for the LAMMPS examples. The LAMMPS example is a little more complicated, users need to open the terminal in jupyter notebook and install matplotlib and LAMMPS logfile in order to run the jupyter notebook. Both of tools are used for benchmark.
```command
pip3 install matplotlib
```
```command
pip3 install lammps-logfile
```

## Warning

If users want to create new examples, key files should be concerned in **.gitignore**.
