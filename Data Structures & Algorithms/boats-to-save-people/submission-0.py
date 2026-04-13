class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i = 0
        j = len(people)-1
        people.sort()
        boat = 0

        while i < j:
            if people[i] + people[j] <= limit:
                boat += 1
                j -= 1
                i += 1
            else:
                boat += 1
                j -= 1
        if i==j:
            boat += 1

        return boat