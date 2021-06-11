#!/bin/bash -l

#$ -cwd


module load python3/recommended

import fibo

fibo.fib(1000)
fibo.fib2(1000)