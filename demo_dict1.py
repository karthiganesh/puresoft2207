import ex015o3_interest as si
#KG220801 Demo for Dictionary
o_a = si.Interest("aaaa",10000,1)
dct_a = {'Borrowser':o_a.s_name,'Principal':o_a.n_principal,'Year':o_a.n_year}
print(dct_a)
dct_b = {'Borrowser':'bbbb','Principal':22222,'Year':2}
o_b = si.Interest(dct_b['Borrowser'],dct_b['Principal'],dct_b['Year'])
o_b.show()