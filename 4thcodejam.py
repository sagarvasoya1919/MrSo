from itertools import combinations
import numpy as np
import sys

def complement(bits): return [
    '_' if b is '_' else 
    '1' if b=='0' else '0' 
    for b in bits
]

class QuantumArray():
    def __init__(self, B):
        self.bits = ['_'] * B
        self.unknown = list(range(B))
        self.read(10)
        self.run()

    def read(self, n):
        for _ in range(n):
            i = self.unknown.pop()
            self.bits[i] = self.read_bit(i+1)
            self.unknown = self.unknown[::-1]
        self.update_states()

    def update_states(self):
        self.cbits  = complement(self.bits)
        self.crbits = self.cbits[::-1]
        self.rbits  = complement(self.crbits)
        self.states = [self.bits, self.cbits, self.crbits, self.rbits]

    def run(self):
        while True:
            self.collapse()
            try: 
                self.read(8)
            except IndexError: 
                break

    def collapse(self):        
        test_idx = self.get_test_idx()
        test = [self.read_bit(i+1) for i in test_idx]
                
        self.bits = next(state
            for state in self.states
            if test == list(np.take(state, test_idx))
        )

    def read_bit(self, i):
        print(i, flush=True)
        return input()
 
    def get_test_idx(self):
        person = list(set(range(B)) - set(self.unknown))
        max_states = len(set(map(tuple, self.states)))
        for idx in combinations(person, 2):
            num_states = len(set(
                tuple(np.take(state, idx))
                for state in self.states
            ))
            if num_states == max_states: 
                return idx

t, B = map(int, input().split())
print('B:', B, file=sys.stderr)
for _ in range(t): 
    array = QuantumArray(B)
    print('guess:', ''.join(array.bits), file=sys.stderr)
    print(''.join(array.bits), flush=True)
    if input() == 'N': 
        sys.exit()
