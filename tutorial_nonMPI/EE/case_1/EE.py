import sys 
sys.path.append('/home/wei-tse/gmxapi_21.4/lib/python3.7/site-packages')
import gmxapi as gmx

EE = gmx.mdrun('sys2_EE.tpr')
EE.run()
