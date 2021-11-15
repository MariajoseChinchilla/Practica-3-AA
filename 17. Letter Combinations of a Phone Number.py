class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        values = { '2':'abc',
               '3':'def',
               '4':'ghi',
               '5':'jkl',
               '6':'mno',
               '7':'pqrs',
               '8':'tuv',
               '9':'wxyz'
    }
        def recursive(i, current):
            if len(current) == len(digits):
                res.append(current)
                return
            for char in values[digits[i]]:
                recursive(i+1,current+char)
        if digits:
            recursive(0,'')
        return res