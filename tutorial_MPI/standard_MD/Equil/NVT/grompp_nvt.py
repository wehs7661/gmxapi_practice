import sys 
import gmxapi as gmx

grompp_nvt = gmx.commandline_operation('gmx_mpi', 
                                     arguments=['grompp'],
                                     input_files={
                                         '-f': 'nvt_equil.mdp',
                                         '-c': '../../EM/sys2_em.gro',
                                         '-p': '../../Topology/sys2.top'},
                                     output_files={'-o': 'sys2_equil.tpr'})
grompp_nvt.run()
print(f'Return code of the process: {grompp_nvt.output.returncode.result()}\n')
if grompp_nvt.output.returncode.result() != 0:
    print(f'Error of the process:\n\n {grompp_nvt.output.erroroutput.result()}')

