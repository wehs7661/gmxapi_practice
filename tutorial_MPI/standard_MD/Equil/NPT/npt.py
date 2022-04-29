import sys 
import gmxapi as gmx

npt = gmx.commandline_operation('gmx_mpi',
                               arguments=['mdrun'],
                               input_files={'-s': 'sys2_equil.tpr'},
                               output_files={
                                   '-c': 'sys2_equil.gro',
                                   '-e': 'equil.edr',
                                   '-g': 'equil.log',
                                   '-o': 'equil.trr',
                                   '-cpo': 'state.cpt'})
npt.run()
print(f'Return code of the process: {npt.output.returncode.result()}\n')
if npt.output.returncode.result() != 0:
    print(f'Error of the process:\n\n {npt.output.erroroutput.result()}')

