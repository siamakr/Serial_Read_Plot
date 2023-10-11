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
        elif self.end == self.n-1:
            self.array[self.end] = elem
            self.end = 0 # shift end delimeter to next pos
        elif self.end < self.n-1:
            self.array[self.end] = elem
            self.end. += 1
            print(f"start: '{self.start}' end: '{self.end}'")
            print(self.array)

    def remove(self):
        if self.end == self.start:
            print('Buffer is empty')

        elif self.start == self.n-1:
            # elem = self.array[self.start]
            self.start = 0
        elif self.start < self.n-1:
            # elem = self.array[self.start]
            self.start += 1
        
        print(f"start: '{self.start}' end: '{self.end}'")
        print(self.array)


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
