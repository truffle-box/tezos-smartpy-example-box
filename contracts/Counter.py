# Counter - Example for illustrative purposes only.

import smartpy as sp

class Counter(sp.Contract):
    def __init__(self, initialValue = 0):
        self.init(storedValue = initialValue)

    @sp.entry_point
    def increment(self, params):
        self.data.storedValue += params.value
    
    @sp.entry_point
    def decrement(self, params):
        self.data.storedValue -= params.value
