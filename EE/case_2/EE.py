import sys 
sys.path.append('/home/wei-tse/gmxapi_21.4/lib/python3.7/site-packages')
import gmxapi as gmx

tpr_list = [f'sys2_EE_{i}.tpr' for i in range(4)]
EE_inputs = gmx.read_tpr(tpr_list)
EE = gmx.mdrun(EE_inputs)
EE.run()
