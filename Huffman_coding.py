class nodetree(object):
  
    def __init__(self,left=None,right=None):
        self.left=left
        self.right=right
        
    def children(self):
        return (self.left,self.right)
      
string = 'AHGHBAGHABHABAGFGHFABAHGHAGF'
freq={}
for char in string:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
freq=sorted(freq.items(),key= lambda x : x[1] ,reverse=True)

def huffman_tree(node,binstring=''):
    if type(node) is str:
        return {node : binstring}
    (l,r)=node.children()
    d={}
    d.update(huffman_tree(l,binstring+'0'))
    d.update(huffman_tree(r,binstring+'1'))
    return d
  
  while len(nodes)>1:
    (k1,c1)=nodes[-1]
    (k2,c2)=nodes[-2]
    nodes=nodes[:-2]
    node=nodetree(k1,k2)
    nodes.append((node,c1+c2))
    nodes = sorted(nodes,key=lambda x : x[1] ,reverse=True)
    
hf=huffman_codetree(nodes[0][0])
for char in hf:
    print(char ," | ",hf[char])
