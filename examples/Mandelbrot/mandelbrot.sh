#!/bin/bash -l
#$ -l h_rt=0:10:0
#$ -l mem=1G
#$ -l tmpfs=15G
#$ -N mandelbrot.sh
#$ -cwd 

module load python3
python3 mandelbrot.py $JOB_ID
