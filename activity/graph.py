import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np


#プロットしたグラフを画像データとして出力するための関数
def Output_Graph():
	buffer = BytesIO()                   
	plt.savefig(buffer, format="png")    
	buffer.seek(0)                       
	img   = buffer.getvalue()            
	graph = base64.b64encode(img)        
	graph = graph.decode("utf-8")        
	buffer.close()
	return graph

#グラフをプロットするための関数
def Plot_Graph(x,y):
	plt.switch_backend("AGG")        
	plt.figure(figsize=(10,5))    
	plt.bar(x,y)                     
	plt.xticks(rotation=45)          
	plt.title("Exercise_Sum_Rank")    
	plt.xlabel("User")               
	plt.ylabel("exercise_time_sum")             
	plt.tight_layout()               
	graph = Output_Graph()           
	return graph

def Output_Graph1():
	buffer = BytesIO()                   
	plt.savefig(buffer, format="png")    
	buffer.seek(0)                       
	img   = buffer.getvalue()            
	graph = base64.b64encode(img)        
	graph = graph.decode("utf-8")        
	buffer.close()
	return graph

def Plot_Graph1(a,b):
	plt.switch_backend("AGG")        
	plt.figure(figsize=(10,5))    
	plt.bar(a,b)                     
	plt.xticks(rotation=45)          
	plt.title("Exercise_done")    
	plt.xlabel("User")               
	plt.ylabel("continue_point")             
	plt.tight_layout()               
	graph = Output_Graph1()           
	return graph


