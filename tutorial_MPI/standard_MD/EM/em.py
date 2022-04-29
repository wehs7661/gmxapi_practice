import sys 
# sys.path.append('/home/wei-tse/gmxapi_21.4/lib/python3.7/site-packages')  # actually not needed
import gmxapi as gmx

em = gmx.commandline_operation('gmx_mpi',
                              arguments=['mdrun'],
                              input_files={'-s': 'sys2_em.tpr'},
                              output_files={
                                  '-c': 'sys2_em.gro',
                                  '-e': 'em.edr',
                                  '-g': 'em.log',
                                  '-o': 'em.trr'})
em.run()
print(f'Return code of the process: {em.output.returncode.result()}\n')
if em.output.returncode.result() != 0:
    print(f'Error of the process:\n\n {em.output.erroroutput.result()}')

