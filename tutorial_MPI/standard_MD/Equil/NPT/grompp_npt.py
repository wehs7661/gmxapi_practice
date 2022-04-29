import sys 
import gmxapi as gmx

grompp_npt = gmx.commandline_operation('gmx_mpi', 
                                     arguments=['grompp'],
                                     input_files={
                                         '-f': 'npt_equil.mdp',
                                         '-c': '../NVT/sys2_equil.gro',
                                         '-p': '../../Topology/sys2.top',
                                         '-t': '../NVT/state.cpt'},
                                     output_files={'-o': 'sys2_equil.tpr'})
grompp_npt.run()
print(f'Return code of the process: {grompp_npt.output.returncode.result()}\n')
if grompp_npt.output.returncode.result() != 0:
    print(f'Error of the process:\n\n {grompp_npt.output.erroroutput.result()}')

