class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = []
        visited = {}
        #print(nums)
        for i in range(0, len(nums)):
            target = -nums[i]
            left, right = i+1, len(nums)-1
            #print(target)
            while left<right:
                #print(target, nums[left], nums[right])
                if target==nums[left]+nums[right]:
                    target_key = ".".join([str(nums[i]), str(nums[left]), str(nums[right])])
                    #print(target_key)
                    if target_key not in visited:
                        answers.append([nums[i], nums[left], nums[right]])
                        visited[target_key]=1
                    left+=1
                    right-=1
                elif target < nums[left]+nums[right]:
                    right-=1
                else:
                    left+=1
        return answers