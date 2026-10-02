class Solution:
    def decodeString(self, s: str) -> str:
        # solution:
        # stack stores [ (previous string, current string repetition times)]
        # when c == number: cur_num = cur_num * 10 + c
        # when c == "[": store into stack [(previous string, number as repetition times)]; then cur_num = 0, cur_string = ""
        # when c == letter: cur_string + c
        # when c == "]": prev_string, repetition_num = stack.pop(); prev_string + cur_string * repetition_num


        cur_str = ""
        cur_num = 0
        stack = [] # store (prev_str, rep_count)
        for c in s:
            if c.isdigit(): # number 
                cur_num = cur_num * 10 + int(c)
            elif c == "[":
                # store in stack
                stack.append((cur_str, cur_num))
                cur_str = ""
                cur_num = 0
            elif c.isalpha(): # letter
                cur_str = cur_str + c
            else: # ]
                prev_str, rep_count = stack.pop()
                cur_str = prev_str + cur_str * rep_count
        return cur_str