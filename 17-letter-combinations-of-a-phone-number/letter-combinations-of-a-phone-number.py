class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
    
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(combination, digits):
            if len(digits) == 0:
                output.append(combination)
            else:
                for letter in mapping[digits[0]]:
                    backtrack(combination + letter, digits[1:])
        output = []
        backtrack('', digits)
        return output
        