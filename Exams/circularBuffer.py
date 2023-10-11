# implement a circular buffer 
# an OOP exam question 

class CircularBuffer:
    def __init__(self, n):
        self.array = [None]*n   # list of length n
        self.n = n
        self.start = 0
        self.end = 0

    def append(self, elem):
        if self.end - self.start == self.n:     # makes sure there is a "removed" position available in array 
            # if end =9 and start = 6 => 3 means full 
            print('Buffer capacity exceeded')
            print(self.array)
        else:
            self.array[self.end % self.n] = elem
            self.end += 1 # shift end delimeter to next pos
            print(f"start: '{self.start}' end: '{self.end}'")
            print(self.array)

    def remove(self):
        if self.end == self.start:
            print('Buffer is empty')
        else:
            elem = self.array[self.start % self.n]
            self.start += 1
            print(f"start: '{self.start}' end: '{self.end}'")
            print(self.array)
            return elem

cb = CircularBuffer(3)
cb.append('a')
cb.append('b')
cb.append('c')
cb.append('d')

cb.remove()
cb.append('d')
cb.append('e')
cb.remove()
cb.remove()
cb.append('l')
cb.append('h')
print(len(cb.array))
cb.append('g')
cb.remove()
cb.append('g')
