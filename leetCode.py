"""
hash each element in J and put this in a set
go through S and see if they're in our set
if it's in the set, then count it 
return the count 
"""

"""
Store elements of J in a set
Iterate through S
for each elem in S
  if elem is in set J
    then increment result
return result

O(n): n == length of the S
O(length of j)
"""
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int: 
        j = set(list(J))
        numJewels = 0
        for s in S: 
			numJewels += 1 if s in j else 0
		return numJewels
