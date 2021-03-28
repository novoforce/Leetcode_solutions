class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #creating a hashmap for encoding the array values
        #we will be storing: arr_value : index_of_that_arr_value into the hashmap
        hashmap= {} 
        
        #looping through the nums array
        for i in range(len(nums)):
            temp= target - nums[i]
            
            #check if the temp is present in the HM or not
            if temp in hashmap:
                #if temp is present then create a temp_list to store the INDICES of the 2 numbers
                temp_list = []
                temp_list.append(hashmap[temp]) #will fetch the index of hashmap[temp]
                temp_list.append(i) #the current no index value
                return temp_list
            #if the temp is not present in HM
            else:
                hashmap[nums[i]] = i