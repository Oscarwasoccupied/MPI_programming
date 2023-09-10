''' Exercise 1: Pair even ranks with odd ranks 
and have each even rank send a message to the corresponding odd rank.
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD
num_PE = comm.Get_size()

my_PE = comm.Get_rank()

if my_PE % 2 == 0:
    my_pair = my_PE + 1
else:
    my_pair = my_PE - 1
    
if my_pair < num_PE:
    if my_PE % 2 == 0:
        message = "Hello, world!"
        comm.send(message, dest=my_pair, tag=0)
    
    if my_PE % 2 != 0:
        message = comm.recv(source=my_pair, tag=0)
        print("PE ", my_PE, " have received ", message)
        