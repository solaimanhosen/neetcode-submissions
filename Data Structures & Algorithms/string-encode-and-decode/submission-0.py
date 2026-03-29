class Solution:
    def encode(self, strs: List[str]) -> str:
        texts = [f"{len(text)}#{text}" for text in strs]

        return "".join(texts)

    def decode(self, s: str) -> List[str]:
        strs: List[str] = list()
        text = str()
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            i = j + 1
            text = s[i:i+length]
            strs.append(text)
            i += length

        return strs
