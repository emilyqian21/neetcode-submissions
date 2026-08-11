class Solution:
    def isValid(self, s: str) -> bool:
        openstack = []
        close2open = {")":"(","}":"{","]":"["}

        for c in s:
            if c not in close2open: # c is open bracket
                openstack.append(c)
            else: # c is close bracket
                if not openstack:
                    return False
                elif close2open[c] != openstack[-1]:
                    return False
                else:
                    openstack.pop()

        return openstack ==[]