class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            #Prefix the length of the string + a delimeter such as #
            res+= str(len(s)) + "#" + s
        return res
    
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0 #Pointer to keep track of which str we at

        while i<len(s):
            #Find where the delimiter # is startig from our currnet position i
            j=i
            while s[j] != "#":
                j+=1
            # The slice s[i:j] gives us the string representation of the length    
            length = int(s[i:j])

            # The actual word starts right after '#' (which is at index j + 1)
            # and ends exactly 'length' characters later
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            # Move our main pointer i to the start of the next encoded block
            i = j + 1 + length
        return res
