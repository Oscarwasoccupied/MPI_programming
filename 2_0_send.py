#!/usr/bin/env python3

from mpi4py import MPI

comm = MPI.COMM_WORLD
worker = comm.Get_rank()
size = comm.Get_size()

# run on 2PES and send a number of 42 from PE0 to PE1l, and let PE0 print the number
if (worker == 0):
    x = 42
    comm.send(x, dest=1)
    print("Hello world from process", worker, " of ", size)
elif (worker == 1):
    x = comm.recv(source=0)
    print("Hello world from process", worker, " of ", size)
    print(x)
    
    
'''
Rank B must know that it is about to receive a message 
and acknowledge this by calling MPI_Recv. 
This sets up a buffer for writing the incoming data 
and instructs the communication device to listen for the message.
The message will not actually be sent before the receiving rank calls MPI_Recv, 
even if MPI_Send has been called.

'''