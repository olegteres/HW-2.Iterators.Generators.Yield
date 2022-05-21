nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f','h',False],
    [1, 2, None],
]

class FlatIterator:
    def __init__(self, lst):
        self.lst = lst
        self.cursor = -1
        self.nest_cursor = 0
        self.list_len = len(self.lst)

    def __iter__(self):
        self.cursor += 1
        self.nest_cursor = 0
        return self

    def __next__(self):
        while self.cursor - self.list_len and self.nest_cursor == len(self.lst[self.cursor]):
          iter(self)
        if self.cursor == self.list_len:
          raise StopIteration
        self.nest_cursor += 1     
        return self.lst[self.cursor][self.nest_cursor - 1]

for item in FlatIterator(nested_list):
	print(item)

if __name__ == '__main__':
  flat_list = [item for item in FlatIterator(nested_list)]
  print(flat_list)



