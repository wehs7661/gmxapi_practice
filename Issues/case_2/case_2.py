import gmxapi as gmx

simulation_input = gmx.read_tpr('sys.tpr')
md = gmx.mdrun(simulation_input)
md.run()

if md.output.returncode.result() != 0:
   print(f'Error of the process:\n\n {md.output.erroroutput.result()}')


