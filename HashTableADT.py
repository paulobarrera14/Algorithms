# HashTable ADT with chaining implementation
# This hashtable accepts only strings and hashes based on their
# ASCII value of the first char
# The constructor takes in the size of the table
# class MyHashtable(object):
#     def __init__(self, size): # Creates an empty hashtable
#         self.size = size
#         # Create the list (of size) of empty lists (chaining)
#         self.table = []
#         for i in range(self.size):
#             self.table.append([])
#     def __str__(self): # for print
#         return str(self.table)
#     def insert(self, elem): # Adds an element into the hashtable
#         hash = ord(elem[0]) % self.size
#         self.table[hash].append(elem)
#     def member(self, elem): # Returns if element exists in hashtable
#         hash = ord(elem[0]) % self.size
#         return elem in self.table[hash]
#     def delete(self, elem): # Removes an element from the hashtable
#         hash = ord(elem[0]) % self.size
#         self.table[hash].remove(elem)

class MyHashtable:
    '''Creates size of hashtable, the table that holds elements and the status table that holds the
    status of each index.'''
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.status = ["empty"] * size

    def __str__(self):
        '''Returns string representation of the main hash table.'''
        return str(self.table)

    def _hash(self,elem):
        '''Hash function, tales the first character of the element and gets the ASCII value, takes
        modulus with size of table. Gives and index in the table.'''
        return ord(elem[0]) % self.size

    def insert(self,elem):
        '''Computes hash value of element, using linear probing to find appropriate slot (looks for "empty" or "deleted").
        If encounters a duplicate it returns without inserting again.'''
        hash_val = self._hash(elem)
        original_hash = hash_val

        while self.status[hash_val] == "filled":
            #item already exists
            if self.table[hash_val] == elem:
                return
            hash_val = (hash_val + 1) % self.size
            #incase table is full
            if hash_val == original_hash:
                raise ValueError("Hash table is full")

        self.table[hash_val] = elem
        self.status[hash_val] = "filled"

    def member(self, elem):
        '''Determins if element exists in the hashtable. If slot is filled with element it returns True, otherwise False.
        If slot is deleted or has different element it uses linear probing until finds the element or encounters empty slot.'''
        hash_val = self._hash(elem)
        original_hash = hash_val

        while self.status[hash_val] != "empty":
            if self.status[hash_val] == "filled" and self.table[hash_val] == elem:
                return True
            hash_val = (hash_val + 1) % self.size
            #travered the entire table
            if hash_val == original_hash:
                return False
        return False

    def delete(self, elem):
        '''Removes an element from the hash table, using hash and linear probing to locate the element.
        Once found it sets the slot in the main table to "None" and updates the status to "deleted."'''
        hash_val = self._hash(elem)
        original_hash = hash_val

        while self.status[hash_val] != "empty":
            if self.status[hash_val] == "filled" and self.table[hash_val] == elem:
                self.table[hash_val] = None
                self.status[hash_val] = "deleted"
                return
            hash_val = (hash_val + 1) % self.size
            if hash_val == original_hash:
                raise ValueError(f"Element {elem} not found in the hash table")

# Testing code
s = MyHashtable(10)
s.insert("amy") #97
s.insert("chase") #99
s.insert("chris") #99
print(s)
print(s.member("amy"))
print(s.member("chris"))
print(s.member("alyssa"))
s.delete("chase")
print(s.member("chris"))
# You can use print(s) at any time to see the contents
# of the table for debugging
print(s)