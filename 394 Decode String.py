class Solution:
    def decodeString(self, s: str) -> str:
        q = []
        long_num = ""
        long_alpha = ""
        
        for i in range(len(s)):
            if s[i] == '[':
                q.append(s[i])
            elif s[i].isdigit():
                long_num = long_num + s[i]
                if s[i+1].isdigit() == False:
                    q.append(long_num)
                    long_num = ""
            elif s[i].isalpha():
                long_alpha = long_alpha + s[i]
                if len(s) == i+1 or s[i+1].isalpha() == False :
                    q.append(long_alpha)
                    long_alpha = "" 
            elif s[i] == "]":
                print("q ", q)
                text = q.pop()
                while True:
                    temp = q.pop()
                    if temp.isalpha() == True:
                        text = temp+text
                    else:
                        break
                        
                
                
                num = q.pop()
                
                res = ""
                for i in range(int(num)):
                    res = res + text
                q.append(res)

        return (''.join(q))