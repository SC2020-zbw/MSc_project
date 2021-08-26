#!/bin/bash -l
#$ -l h_rt=0:10:0
#$ -l mem=1G
#$ -l tmpfs=15G
#$ -N LAMMPS.sh
#$ -cwd 

#$ -pe mpi 8
module load python3
module load compilers/intel/2018/update mpi/intel/2018/update3/intel lammps/7Aug19/basic/intel-2018
gerun  lmp_default -in in.rhodo.scaled -log log.lammps.
