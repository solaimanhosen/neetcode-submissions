class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token not in "+-*/":
                st.append(int(token))
            else:
                b = st.pop()
                a = st.pop()
                if token == "+":
                    st.append(a + b)
                elif token == '-':
                    st.append(a - b)
                elif token == "*":
                    st.append(a * b)
                else:
                    st.append(math.trunc(a / b))

        return st[0]
