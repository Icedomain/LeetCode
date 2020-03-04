import os
import numpy
mycode = os.listdir('../src/Python/')
mycode = sorted(mycode,key = lambda x: int(x.split('.')[0]) )

filename = 'python.tex'
with open(filename, 'w') as file_object:
    for file in mycode:
        res = "\lstinputlisting[language=Python]{" + f'../src/Python/{file}' + "}\n"
        print(res)
        file_object.write(res)
        #break

mycode = os.listdir('../src/Cplusplus/')
mycode = sorted(mycode,key = lambda x: int(x.split('.')[0]) )

filename = 'cpp.tex'
with open(filename, 'w') as file_object:
    for file in mycode:
        res = "\lstinputlisting[language=Python]{" + f'../src/Cplusplus/{file}' + "}\n"
        print(res)
        file_object.write(res)
        #break



