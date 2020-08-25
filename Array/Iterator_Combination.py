"""

Design an Iterator class, which has:
A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false

"""

class CombinationIterator:

    def __init__(self, characters: str, n: int):
        self.string = characters
        self.l = len(characters)
        # getting all combinaion of binary string of length l and no of set bits = n
        self.combination = self.SuitableBinary(n)
        # get no of such binary no which are suitable, numers are in sequence suitable for lexiographic order
        self.comb_length = len(self.combination)
        self.index = 0
        
    def next(self) -> str:
        comb = self.combination[self.index]
        self.index += 1
        return self.BinaryToString(comb)

    def hasNext(self) -> bool:
        return self.index < self.comb_length
        
    
    def SuitableBinary(self,target):
        # do not start form 1<<length as it contain 1 extra binary digit and always put (1<<length)-1 
        # start from num and go to 0 to get lexiographic ordering in string
        num = (1<<len(self.string))-1
        comb = []
        while num:
            b = bin(num)[2:]
            if b.count('1') == target:
                comb.append(b.zfill(self.l))
            num -= 1
        # print(comb)
        return comb
    
    def BinaryToString(self,comb):
        result = ""
        for i in range(self.l):
            if comb[i] == '1':
                result += self.string[i]
        return result
        
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
