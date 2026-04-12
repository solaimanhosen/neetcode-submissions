class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for ops in operations:
            if ops == "+":
                st.append(st[-1] + st[-2])
            elif ops == "C":
                st.pop()
            elif ops == "D":
                st.append(st[-1] * 2)
            else:
                st.append((int(ops)))

        return sum(st)
