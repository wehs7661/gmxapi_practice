import sys 
# sys.path.append('/home/wei-tse/gmxapi_21.4/lib/python3.7/site-packages')  # actually not needed
import gmxapi as gmx

grompp_em = gmx.commandline_operation('gmx_mpi', 
                                     arguments=['grompp'],
                                     input_files={
                                         '-f': 'em.mdp',
                                         '-c': '../Sol/sys2_sol.gro',
                                         '-p': '../Topology/sys2.top'},
                                     output_files={'-o': 'sys2_em.tpr'})
grompp_em.run()


print(f'Return code of the process: {grompp_em.output.returncode.result()}\n')
if grompp_em.output.returncode.result() != 0:
    print(f'Error of the process:\n\n {grompp_em.output.erroroutput.result()}')

