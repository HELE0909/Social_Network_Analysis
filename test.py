__author__ = 'multiangle'

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from DB_Interface import MySQL_Interface

dbi=MySQL_Interface()
[select_user,select_user_col]=dbi.select_all('selected_user')
user_list= [line[select_user_col.index('uid')] for line in select_user]
[atten_web,atten_web_col]=dbi.select_all('temp_table')
atten_list=[[line[atten_web_col.index('from_uid')],line[atten_web_col.index('to_uid')]] for line in atten_web]
sig_list= [line[0]+line[1] for line in atten_list]
select_atten_list=[]
for line in atten_list:
    temp_sig_a=line[0]+line[1]
    temp_sig_b=line[1]+line[0]
    if temp_sig_a in sig_list and temp_sig_b in sig_list :
        select_atten_list.append(line)

# int_atten_list=[]
# for line in atten_list:
#     if line[0] in user_list and line[1] in user_list:
#         temp=[]
#         temp.append(user_list.index(line[0])+1)
#         temp.append(user_list.index(line[1])+1)
#         int_atten_list.append(tuple(temp))

G=nx.Graph()
# nodes=list(range(1,user_list.__len__()+1))
# G.add_nodes_from(nodes)
G.add_nodes_from(user_list)
# G.add_edges_from(int_atten_list)
G.add_edges_from(select_atten_list)
# L = nx.normalized_laplacian_matrix(G)
# e = np.linalg.eigvals(L.A)
# e=sorted(e,reverse=True)
# print(nx.clustering(G))
# plt.plot(e,'.')
nx.draw(G,node_size=30)
plt.show()

# path='F:\\multiangle\\Coding!\\pro\\社交网络分析\\海豚社交数据集\\dataset_100867\\DataSet\\dolphins.txt'
# f=open(path,'r')
# line=f.readline()
# edge=[]
# while line:
#      if line.__len__()>1:
#          line.strip()
#          line=line[0:-1]
#          line=line.split(' ')
#          line=[int(x) for x in line]
#          edge.append(tuple(line))
#      line=f.readline()
#
# nodes=list(range(1,62))
#
# G=nx.Graph()
#
# G.add_nodes_from(nodes)
# G.add_edges_from(edge)
# L = nx.normalized_laplacian_matrix(G)
# e = np.linalg.eigvals(L.A)
# #print(nx.clustering(G))
#
# nx.draw(G)
# plt.show()

# plt.show()
# print(G.size())
# print(nx.k_components(G))
