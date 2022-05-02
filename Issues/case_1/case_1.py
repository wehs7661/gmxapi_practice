import gmxapi as gmx

md = gmx.commandline_operation('gmx_mpi',
                               arguments=['mdrun', '-deffnm', 'sys'],
                               input_files={'-s': 'sys.tpr'})
md.run()

print(f'Return code of the process: {md.output.returncode.result()}\n')

if md.output.returncode.result() != 0:
   print(f'Error of the process:\n\n {md.output.erroroutput.result()}')

