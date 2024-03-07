class Solution:
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    ans = []

    def helper(k, n, s, path):
      if k == 0 and n == 0:
        ans.append(path)
        return
      if k == 0 or n < 0:
        return

      for i in range(s, 10):
       helper(k - 1, n - i, i + 1, path + [i])

    helper(k, n, 1, [])
    return ans