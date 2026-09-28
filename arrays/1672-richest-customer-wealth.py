class Solution:
    def maximumWealth(self, accounts ):
        wealth=[]

        for i in accounts:
            wealth.append(sum(i))
        return max(wealth)
