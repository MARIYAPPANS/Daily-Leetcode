class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = total_cost = 0
        current_gas = 0
        start = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += gas[i] - cost[i]
            
            if current_gas < 0:
                # If we can't reach the next station, reset the start point
                start = i + 1
                current_gas = 0
        
        return start if total_gas >= total_cost else -1
