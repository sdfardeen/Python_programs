class Solution:

    def length_of_longest_sub_string(self, s: str) -> str:

        longest_str = ""
        for i, c in enumerate(s):
            candidate_str = str(c)
            for j in range(i + 1, len(s)):
                if s[j] not in candidate_str:
                    candidate_str += str(s[j])
                else:
                    break
            if len(candidate_str) > len(longest_str):
                longest_str = candidate_str
            if len(s) - i <= len(longest_str):
                break
        return longest_str


s = Solution()
print(s.length_of_longest_sub_string("asdedfasdfadegtgad"))
