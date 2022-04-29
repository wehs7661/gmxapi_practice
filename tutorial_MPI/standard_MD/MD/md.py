import sys 
import gmxapi as gmx

md = gmx.commandline_operation('gmx_mpi',
                              arguments=['mdrun'],
                              input_files={'-s': 'sys2_md.tpr'},
                              output_files={
                                  '-c': 'sys2_md.gro',
                                  '-e': 'md.edr',
                                  '-g': 'md.log',
                                  '-o': 'md.trr'})
md.run()
print(f'Return code of the process: {md.output.returncode.result()}\n')
if md.output.returncode.result() != 0:
    print(f'Error of the process:\n\n {md.output.erroroutput.result()}')

