import sys 
# sys.path.append('/home/wei-tse/gmxapi_21.4/lib/python3.7/site-packages')  # actually not needed
import gmxapi as gmx

box = gmx.commandline_operation('gmx_mpi',
                               arguments=['editconf', '-bt', 'dodecahedron', '-d', '1', '-c'],
                               input_files={'-f': '../sys2_init.gro'},
                               output_files={'-o': 'sys2_box.gro'})
box.run()
print(f'Return code of the process: {box.output.returncode.result()}\n')
if box.output.returncode.result() != 0:
    print(f'Error of the process:\n\n {box.output.erroroutput.result()}')

