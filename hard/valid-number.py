class Solution:
    def isNumber(self, s: str) -> bool:
        def remove_sign(cs: str) -> str:
            return cs[1:] if cs and cs[0] in ('-', '+') else cs

        def is_integer(cs: str) -> bool:
            return remove_sign(cs).isdigit()

        def is_decimal(cs: str) -> bool:
            ps = remove_sign(cs).split('.')
            return len(ps) == 2 and any(ps) and all(not p or p.isdigit() for p in ps)

        num, *exponents = s.replace('E', 'e').split('e')
        return ((is_integer(num) or is_decimal(num))
                and (not exponents or (len(exponents) == 1 and is_integer(exponents[0]))))
