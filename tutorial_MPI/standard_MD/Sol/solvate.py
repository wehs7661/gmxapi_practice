import sys 
# sys.path.append('/home/wei-tse/gmxapi_21.4/lib/python3.7/site-packages')  # actually not needed
import gmxapi as gmx

solvate = gmx.commandline_operation('gmx_mpi',
                                   arguments=['solvate', '-cs'],
                                   input_files={
                                       '-cp': '../Box/sys2_box.gro',
                                       '-p': '../Topology/sys2.top'},
                                   output_files={'-o': 'sys2_sol.gro'})
solvate.run()
print(f'Return code of the process: {solvate.output.returncode.result()}\n')
if solvate.output.returncode.result() != 0:
    print(f'Error of the process:\n\n {solvate.output.erroroutput.result()}')

