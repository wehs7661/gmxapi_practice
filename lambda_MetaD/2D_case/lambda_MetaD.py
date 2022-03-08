import sys 
sys.path.append('/home/wei-tse/gmxapi_21.4/lib/python3.7/site-packages')
import gmxapi as gmx

lambda_MetaD = gmx.commandline_operation('gmx',
                              arguments=['mdrun', '-plumed', '../plumed_2.dat'],
                              input_files={'-s': '../sys2_lambda.tpr'},
                              output_files={
                                  '-c': '../sys2_lambda.gro',
                                  '-e': '../lambda.edr',
                                  '-g': '../lambda.log',
                                  '-o': '../lambda.trr'})
lambda_MetaD.run()

if lambda_MetaD.output.returncode.result() != 0:
    print(f'STDERR of the process:\n\n {lambda_MetaD.output.stderr.result()}\n')
else:
    print('The process was executed successfully.')
