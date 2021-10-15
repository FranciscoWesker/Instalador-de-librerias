from subprocess import call

print ("""

SS8t8%8%8t8%8%8t8%8%8t8%8%%%%%%%%%%%%%%S      Instalador de librerias:
S                         St%t%t%t%t%t%%                
S                         %t%t%%%t%%%t%%      [1] Numpy
S                         S%t%t%t%t%t%t%                
S                         St%t%t%t%t%t%%      [2] Pandas
S                         St%%%t%%%t%%tS                 
S                         S%t%t%t%t%t%t%      [3] Matplotlib
S            . . . . . .  %t%%%t%t%t%t%%  
S         . :8@ %  SSSSX% S@ @S@8888X8 S      [4] numba
%          . 8   tt:t;;;:t  ;.;%tt;:; @:
S8       .  :  %............. .......  :      [5] shap
%t     .     ..@ ;.               .    t              
%%8 . .   .     %8:. .  . .  . . ..8  .%      [6] bokeh
%: 8%.   .    . %X...           ..%  :%%
%%;:;X8:  . .. ..X8%. .  . . . . t  tt%%      [7] Posible error al instalar
%%%t:  ;8;    .  :88           . S ;%ttS
%t%%tt%t;;t@8@88    8;. .  .  .    t%%%%      [8] Salir
%%t%t%%t%%;:.  .;;;. %..     ..8  t%t%tS
%%%t%t%%t%%%t%t%%t%t:  .. . . X  t%%t%t%
%t%t%tt%t%t%t%%t%t%%tt8  .  .:8 %%t%t%%S
%%t%%%%t%t%t%t%t%t%t%t:8  ..:8 tt%t%%%t%
%%%t%t%t%t%%%t%t%%%t%%t; .:   :%%%t%t%%%
%t%t%t%t%%%t%t%%%t%t%t%: 8:8  %%t%t%t%tS
%%t%t%t%t%t%t%t%t%t%t%t%;.   t%%t%t%t%%%
%%%S8%8%8%%8 8%8%8%%8 %%%: ;%%%%%8%%8t%%
                                         Francisco Salgado Castaño
                                         Edilson Lopez y Sofia Cordoba Rojas
""")
ans=True
ens=False
while ans !=8:
  ans=int(input("Seleccione una opcion: "))
  if ans==1:
   print ("""Instalando Numpy....
          import numpy as np #Importamos numpy como np
""") 
   print(call(["pip","install","numpy"]))

  elif ans==2:
    print ("""Instalando Pandas...
              import pandas as pd  #Importamos pandas como pd
              import numpy as np   #Tambien lo podenmos importar como np
""")
    print(call(["pip","install","pandas"]))

  elif ans==3:
    print ("""Instalando Matplotlib...
            import matplotlib.pyplot as plt #Importamos Matplotlib como plt
""")
    print(call(["pip","install","matplotlib"]))

  elif ans==4:
     print ("""Instalando Numba...
               from numba import jit #importamos Numba como jit
           """)
     print(call(["pip","install","numba"]))
  elif ans==5:
     print ("""Instalando shap...
            import shap #Importamos shap como shap""")
     print(call(["pip","install","shap"]))
  elif ans==6:
    print ("Intalando bokeh...")
    print(call(["pip","install","bokeh"]))
  elif ans==7:
    print ("""
El problema está en la ubicación del PATH.
https://www.kyocode.com/2019/10/agregar-python-path-windows/
si esto te funciona entonces prueba reinstalando python.
En el instalador te la opcion de agregar el PATH.""")


  elif ans==8:
    salir = True

