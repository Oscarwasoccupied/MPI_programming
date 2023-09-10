from mpi4py import MPI
number_to_send = 4
total = 0
my_pe_num = MPI.COMM_WORLD.Get_rank()

if my_pe_num == 0:
    for destination in range(1,4):
        MPI.COMM_WORLD.send(number_to_send, dest=destination, tag=0)
else:
    number_received = MPI.COMM_WORLD.recv(source=0, tag=0)
    result = number_received * my_pe_num

for pe in range(1,4):
    MPI.COMM_WORLD.barrier()
    if pe == my_pe_num:
        print("PE ", my_pe_num,"'s result is ", result)

# MPI.COMM_WORLD.barrier()
if my_pe_num == 0:
    for sender in range(1,4):
        result = MPI.COMM_WORLD.recv(source=sender, tag=0)
        total += result
    print("Total is ", total,"\n")
else:
    MPI.COMM_WORLD.send(result, dest=0, tag=0)
