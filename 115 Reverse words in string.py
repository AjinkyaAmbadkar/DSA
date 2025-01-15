class Solution:
    # Approach:
    # 1. Loop from last charachter to first
    # 2. Exact word in reverse order and make them as it is originally
    # 3. Scan util space as we also want one space in between words in string
    # 4. for last word reverse it manually outside the loop
    # 5. Use trim function to remove extra spaces from string and join them back and return
    def reverseWords(self, s: str) -> str:
        resultString = ""
        tempWord = ""
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                tempWord += s[i]
            else:
                word = tempWord[::-1]
                print(word)
                resultString += word
                resultString += " "
                tempWord = ""
        word = tempWord[::-1]
        # print(word)
        resultString += word
        # resultString += " "
        # print(resultString)
        words = resultString.split()
        newResultString = " ".join(words)
        return newResultString
