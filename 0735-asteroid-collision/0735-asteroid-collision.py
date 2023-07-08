class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack: List[int] = []
        for asteroid in asteroids:
            if len(stack) == 0:
                stack.append(asteroid)
            else:
                last_asteroid = stack[-1]
                if not (last_asteroid > 0 and asteroid < 0):
                    stack.append(asteroid)
                else:
                    ast_size = abs(asteroid)
                    last_ast_size = abs(last_asteroid)
                    while last_ast_size <= ast_size:
                        if last_ast_size == ast_size:
                            stack.pop()
                            break
                        else:
                            stack.pop()
                            if len(stack) == 0:
                                stack.append(asteroid)
                                break
                            else:
                                last_ast_size = abs(stack[-1])
                                last_asteroid = stack[-1]
                                if last_asteroid < 0:
                                    stack.append(asteroid)
                                    break
        return stack



