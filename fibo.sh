#!/bin/bash -l

module load python3/recommended

import fibo

fibo.fib(1000)
fibo.fib2(1000)