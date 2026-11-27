class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #A clever way to solve this is to sort the list first; find the sum of nums[i], nums[j] and nums[k]. If sum == 0, append it to our result; elif sum < 0, move right (increment); else, move left (decrement). 

        #Sorting the list makes it easier to know which pointer to move.
        #Find all possible DIFFERENT (skipping duplicates) combinations of nums[j] and nums[k] for i. 
        
        #Exit inner loop and proceed with the outer loop; if nums[i] was already used continue with the loop and work with a different nums[i]. If we find a valid triplet, we move both pointers and only then we check and skip duplicates of j and k.

        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i+1
            k = len(nums)-1

            while j < k:
                target = nums[i] + nums[j] + nums[k]

                if target == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                
                elif target < 0:
                    j += 1
                
                else:
                    k -=1
        return result