
lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
counting=list(map(lambda x,y:[x.count("A"),y.count("a")],lst1,lst1))
print(counting)
