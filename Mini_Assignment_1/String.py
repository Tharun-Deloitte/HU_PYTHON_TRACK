class StringClass:
    def __init__(self, st):
        self.st = st

    def length(self):
        return len(self.st)

    def list_convert(self):
        return list(self.st)


class PairsPossible(StringClass):
    def pair(self, demo_list):
        answer = [(n, j) for idx, n in enumerate(demo_list) for j in demo_list[idx:]]
        return answer


class SearchCommonElements(StringClass):

    def common(self, st2, st):
        removed = list(set(st2) & set(st))
        print('Commons from two strings')
        print(removed)


class EqualSumPairs():
    def count(self, res_list):
        lst = []
        for tup in res_list:
            sum = 0
            for i in tup:
                sum += int(i)
            lst.append(sum)
        print('Pairs having unique sums')
        print(set(lst))
        print(len(set(lst)))




st = input("Enter a string :")
send1 = StringClass(st)
print('Length of string')
print(send1.length())
print('Convert string to list')
print(send1.list_convert())

sc_list = send1.list_convert()
send2 = PairsPossible(send1)
result = send2.pair(sc_list)
print('All possible pairs')
print(result)

st2 = input("Enter a string :")
send3 = SearchCommonElements(send1)
send3.common(st2, st)

send4 = EqualSumPairs()
send4.count(result)
