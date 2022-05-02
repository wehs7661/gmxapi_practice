import gmxapi as gmx

tpr_list = ['sys.tpr' for i in range(16)]
simulation_input = gmx.read_tpr(tpr_list)
md = gmx.mdrun(simulation_input)
md.run()
