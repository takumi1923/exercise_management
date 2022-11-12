import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np

def Output_Graph2():
	buffer = BytesIO()                   
	plt.savefig(buffer, format="png")    
	buffer.seek(0)                       
	img   = buffer.getvalue()            
	graph = base64.b64encode(img)        
	graph = graph.decode("utf-8")        
	buffer.close()
	return graph

def Plot_Graph2(a,b):
	plt.switch_backend("AGG")        
	plt.figure(figsize=(10,5))    
	plt.bar(a,b)                     
	plt.xticks(rotation=45)          
	plt.title("Ikusei_Sum")    
	plt.xlabel("User")               
	plt.ylabel("Ikusei_Huyo_Point")             
	plt.tight_layout()               
	graph = Output_Graph2()           
	return graph