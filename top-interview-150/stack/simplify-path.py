class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        for p in path.split('/'):
            if p == '..' and ans:
                ans.pop()
            if p not in ('', '.', '..'):
                ans.append(p)
        return '/' + '/'.join(ans)
