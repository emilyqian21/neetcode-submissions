class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # solution: simulation / DP
        #
        # main logic:
        # 1. first and last element of each row are always 1
        # 2. each inner element is the sum of two elements
        #    from the previous row
        #
        # current_row[j] = previous_row[j - 1] + previous_row[j]

        res = []

        for i in range(numRows):
            # row i has i + 1 elements
            current_row = [1] * (i + 1)

            # fill in the inner elements
            if i > 0:
                previous_row = res[i - 1]

                for j in range(1, i): # j代表每行的element, 然后跳过第一个和最后一个，因为第一个和最后一个就是永远是1
                    current_row[j] = ( previous_row[j - 1] + previous_row[j])

            res.append(current_row)

        return res