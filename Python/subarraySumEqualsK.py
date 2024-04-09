class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        psCount = defaultdict(int)
        ps = 0
        psCount[0] = 1
        count = 0

        for num in nums:
            ps += num
            req = ps-k

            if req in psCount:
                count += psCount[req]

            psCount[ps] += 1

        return count