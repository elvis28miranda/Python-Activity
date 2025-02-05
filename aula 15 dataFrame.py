import pandas as pd
import numpy as np

#dataframe a partir de um array --------------------------------------------------

arr = np.random.randint(10,55,size=(4,4))

df1 = pd.DataFrame(data=arr, index=['A','B','C','D'], columns=['W','X','Y','Z'])

#criação de DF a partir de lista--------------------------------------------------

lista = [[10,20,30,40,50],[60,70,80,90,100]]

df2 = pd.DataFrame(data=lista,index=['A','B'],columns = ['V','W','X','Y','Z'])


#criação de DF atraves de dicionário--------------------------------------------------

dados = {'produtos':['VideoGame','PC','teclado','mouse','microfone'],'preço':[2600,2450.90,99.90,75,129.90]}

df3 = pd.DataFrame(data = dados)

#criação de uma nova coluna--------------------------------------------------

df3['Custo'] = [1900,2000,40,56.50,95.4]

df3['Lucro'] = df3['preço'] = df3['Custo'] 





