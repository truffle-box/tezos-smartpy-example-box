# Migrations - Example for illustrative purposes only.

import smartpy as sp

class Migrations(sp.Contract):
    def __init__(self, last_completed_migration = 0):
        self.init(last_completed_migration = last_completed_migration)

    @sp.entry_point
    def main(self, completed):
        self.data.last_completed_migration = completed
