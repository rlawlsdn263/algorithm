class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = ""
        shortest_str = min(strs, key=len)

        for i in range(len(shortest_str)):
          current_char = shortest_str[i]
          for j in range(len(strs)):
            if strs[j][i] != current_char:
              return prefix
          prefix += current_char

        return prefix