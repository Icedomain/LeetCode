import os
import numpy

### python部分

mycode = [i for i in os.listdir('../src/Python/') if i.endswith('.py')]
num = len(mycode)
mycode = sorted(mycode,key = lambda x: int(x.split('.')[0]) )

filename = 'python.tex'
with open(filename, 'w') as file_object:
    kaitou = f"本文档一共统计了{num}道题\n"
    file_object.write(kaitou)
    for file in mycode:
        res = "\lstinputlisting[language=Python]{" + f'../src/Python/{file}' + "}\n" # + "\\newpage\n"
        print(res)
        file_object.write(res)
        #break


### c++部分
mycode = [i for i in os.listdir('../src/Cplusplus/') if i.endswith('.cpp')]
num = len(mycode)
mycode = sorted(mycode,key = lambda x: int(x.split('.')[0]) )

filename = 'cpp.tex'
with open(filename, 'w') as file_object:
    kaitou = f"本文档一共统计了{num}道题\n"
    file_object.write(kaitou)
    for file in mycode:
        res = "\lstinputlisting[language=C++]{" + f'../src/Cplusplus/{file}' + "}\n"
        print(res)
        file_object.write(res)
        #break



