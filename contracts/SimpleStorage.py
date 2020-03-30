# SimpleStorage - Example for illustrative purposes only.

import smartpy as sp

class SimpleStorage(sp.Contract):
    def __init__(self, initialValue = 0):
        self.init(storedValue = initialValue)

    @sp.entry_point
    def set(self, params):
        self.data.storedValue = params.newValue
