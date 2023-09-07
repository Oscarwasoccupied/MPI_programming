#!/usr/bin/env python3

from mpi4py import MPI

comm = MPI.COMM_WORLD
worker = comm.Get_rank()
size = comm.Get_size()
x = 2

print("Hello world from process", worker, " of ", size)
print(x)
if (worker == 0):
    x = 0

print(x)    