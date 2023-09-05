#!/usr/bin/env python3

from mpi4py import MPI

comm = MPI.COMM_WORLD
worker = comm.Get_rank()
size = comm.Get_size()

print("Hello world from process", worker, " of ", size)