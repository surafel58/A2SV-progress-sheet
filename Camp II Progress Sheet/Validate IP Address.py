class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ans = ""
        
        def validateFour(input):
            input = input.split(".")
            
            for value in input:
                if len(input) != 4 or not (0 < len(value) <= 3) or (not value.isnumeric()) or (len(value) > 1 and value[0] == "0"):
                    return "Neither"
                try: 
                    if not (0 <= int(value) <= 255):
                        return "Neither"
                except: 
                    return "Neither"

            return "IPv4"
                

        def validateSix(input):
            
            input = input.split(":")

            for value in input:
                if not 0 < len(value) <= 4 or len(input) > 8:
                    return "Neither"
                for char in value:
                    if not char.isdecimal() and not "A" <= char <= "F" and not "a" <= char <= "f":
                        
                        return "Neither"

            return "IPv6"
        
        if queryIP.find(".") != -1:
            ans = validateFour(queryIP)
        else:
            ans = validateSix(queryIP)
        
        return ans
