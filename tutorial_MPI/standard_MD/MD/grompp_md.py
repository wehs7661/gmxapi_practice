import sys 
import gmxapi as gmx

grompp_md = gmx.commandline_operation('gmx_mpi', 
                                     arguments=['grompp'],
                                     input_files={
                                         '-f': 'md.mdp',
                                         '-c': '../Equil/NPT/sys2_equil.gro',
                                         '-p': '../Topology/sys2.top',
                                         '-t': '../Equil/NPT/state.cpt'},
                                     output_files={'-o': 'sys2_md.tpr'})
grompp_md.run()
print(f'Return code of the process: {grompp_md.output.returncode.result()}\n')
if grompp_md.output.returncode.result() != 0:
    print(f'Error of the process:\n\n {grompp_md.output.erroroutput.result()}')

