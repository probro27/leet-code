class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        pathSplit = path.split('/')

        for folder in pathSplit:
            if folder == '' or folder == '.':
                continue
            elif folder == '..':
                if len(stack) > 0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(folder)
        
        if len(stack) == 0:
            return '/'
        else:
            final_path = ''
            for folder in stack:
                final_path += f'/{folder}'
            return final_path
