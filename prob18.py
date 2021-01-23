#Unfinished
neighbors = []
prev_index = 1
nums = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


nums = nums.split("\n")
#Convert to list of lists in correct format
for i in range(len(nums)):
    nums[i] = list(nums[i].split(" "))
    nums[i] = [int(j) for j in nums[i]]

#Hard code the first two numbers because its the only one that doesnt fit the pattern
neighbors.append(int(nums[0][0]))
neighbors.append(int(nums[1][0]))

for i in range(2,15):
    neighbors.append(max(int(nums[i][prev_index-1]),int(nums[i][prev_index+1])))
    prev_index = nums[i].index(max(int(nums[i][prev_index-1]),int(nums[i][prev_index+1])))
    #neighbors.append(int(nums[i][i-1]))

print("NEIGHBORS: ",neighbors)
print("SUM: ", sum(neighbors))
