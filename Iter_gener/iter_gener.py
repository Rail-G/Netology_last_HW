
"""ГЕНЕРАТОР"""

def flat_generator(lis):
    for i in lis:
        if isinstance(i, list):
            for i in flat_generator(i):
                yield i
        else: 
            yield i


"""ИТЕРАТОР"""

class FlatIterator():
    
    def __init__(self, lists):
        self.lists = lists
        self.count = 0
        self.len_list = self.itera(self.lists)

    def __iter__(self):
        return self
    
    def itera(self, lst):
        flat = []
        for i in lst:
            if isinstance(i, list):
                flat.extend(self.itera(i))
            else: 
                flat.append(i)
        return flat

    def __next__(self):
        if self.count < len(self.len_list):
            current = self.len_list[self.count]
            self.count += 1
            return current
        else:
            raise StopIteration
