''' Exercise 2: each rank sends its message to rank 0. 
Have rank 0 print each message.
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD
num_PE = comm.Get_size()

my_PE = comm.Get_rank()

if my_PE != 0:
    message = "Hello, world!"
    comm.send(message, dest=0, tag=0)
else:
    for i in range(1,num_PE):
        message = comm.recv(source=i, tag=0)
        print("PE ", my_PE, " have received ", message, " from PE ", i)
    
        