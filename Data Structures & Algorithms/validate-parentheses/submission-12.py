class Solution:
    def isValid(self, s: str) -> bool:
        openstack = [] # store open parenthesis
        close2open = {"}" : "{", ")" : "(", "]" : "["}

        for c in s:
            if c in close2open.values(): # it's open parenthesis
                openstack.append(c)

            elif c in close2open: # it's close parenthesis 
                if not openstack:
                    return False
                if close2open[c] != openstack[-1]:
                    return False
                else:
                    openstack.pop()

        return len(openstack) == 0 #avoid object compare object. when possible, compare len