class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        interval_start = nums[0]
        intervals = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                intervals.append((interval_start, nums[i-1]))
                interval_start = nums[i]
        intervals.append((interval_start, nums[-1]))
        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[0] == interval[1]:
                intervals[i] = str(interval[0])
            else:
                intervals[i] = "{}->{}".format(interval[0], interval[1])
        return intervals


solution = Solution()
assert solution.summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
assert solution.summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
