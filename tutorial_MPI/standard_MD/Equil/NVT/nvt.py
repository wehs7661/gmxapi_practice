import sys 
import gmxapi as gmx

nvt = gmx.commandline_operation('gmx_mpi',
                               arguments=['mdrun'],
                               input_files={'-s': 'sys2_equil.tpr'},
                               output_files={
                                   '-c': 'sys2_equil.gro',
                                   '-e': 'equil.edr',
                                   '-g': 'equil.log',
                                   '-o': 'equil.trr',
                                   '-cpo': 'state.cpt'})
nvt.run()
print(f'Return code of the process: {nvt.output.returncode.result()}\n')
if nvt.output.returncode.result() != 0:
    print(f'Error of the process:\n\n {nvt.output.erroroutput.result()}')

