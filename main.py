nums = [3, 2, 4]
target = 6
def Output(nums, target):
    output = 'Нет такой пары'
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if target == nums[i] + nums[j]:
                output = 'Индекс: ' + str(i) + ' и ' + str(j)
    return output
print(Output(nums, target))
