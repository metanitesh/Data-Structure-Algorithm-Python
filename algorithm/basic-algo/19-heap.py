class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]        # initialize arrays
        self.next_index = 0                                   # denotes next index where new element should go
    
    def insert(self, data):

        self.cbt[next_index] = data
        next_index += 1;

        """
        Insert `data` into the heap
        """
        pass