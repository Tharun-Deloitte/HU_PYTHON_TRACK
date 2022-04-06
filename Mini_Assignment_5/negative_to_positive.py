lst1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
negative_num=list(map(lambda x:abs(x),(filter(lambda x:x<0,map(lambda x:x,lst1)))))
print(negative_num)
