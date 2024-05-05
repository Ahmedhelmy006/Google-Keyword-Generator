import pandas as pd

def adjust_text_layout(text):
    if isinstance(text, str): 
        elements = text.split(", ")[:10] 
        return elements  
    else:
        return [""]  

chunks = pd.read_csv("Products.csv", encoding="latin1", chunksize=1000)
dfs = []
for chunk in chunks:
    try:
        chunk["Result"] = chunk["Result"].apply(adjust_text_layout)
        dfs.append(chunk)
    except Exception as e:
        print("Error:", e)

df = pd.concat(dfs)

df.to_csv("Modified_Products.csv", index=False)
