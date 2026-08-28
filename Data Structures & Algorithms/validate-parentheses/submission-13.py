class Solution:
    def isValid(self, s: str) -> bool:
        close2open = {")" : "(", "}" : "{", "]":"["}
        openstack =  []

        for c in s:
 
            if c in close2open: # c is close
                if openstack == []:
                    return False
                if openstack[-1] != close2open[c]: # open to be matched in openstack is not the same as the close2open[c]; if openstack["{"], close2open[c] = "("
                    return False
                openstack.pop() # success match, pop the openstack[-1]
            else: # open
                openstack.append(c)
        return openstack == []