'''You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.'''

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        self.word1=word1
        self.word2=word2
        merged=''
        i=0
        j=0
        while i<len(word1) and j<len(word2):
            merged+=word1[i]
            merged+=word2[j]
            i+=1
            j+=1
        merged+=word1[i:]
        merged+=word2[j:]
                
        return merged
                

msg=Solution()
print(msg.mergeAlternately('ab','pqrs'))
