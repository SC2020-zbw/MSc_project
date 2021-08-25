# MSc project: Integrating Jupyter with UCL HPC systems

## Python library for job schedule in jupyter notebook front end of HPC system **Myriad**

There is a **job** class in **sge** library to control the job while interacting with **Myriad** in jupyter notebook front end. 

## Goals

 * A Job class representing a Grid Engine job in Python
 * Routines for submitting, deleting, querying jobs, retrieving output etc
 * Routines for monitoring queue status
 * Sub-classes with common applications
 * Submitting kernels from the notebook into a job

 ## Examples

There are two examples in the folder **examples**. Mandelbrot and LAMPPS

### Mandelbrot

 ```python

 ```

The python file to generate Mandelbrot set and to plot the figure are created without using library, the rest of work is to generate the scripts then submit the job in **Myriad** and finally check the output as well as returning figure.
