class Solution:
    def recursiveFill(self, image: List[List[int]], sr: int, sc: int, newColor: int, prev: str) -> List[List[int]]:
        start = image[sr][sc]
        if start == newColor:
            return image
        image[sr][sc] = newColor
        if sr > 0 and sr < len(image) - 1:
            if sc > 0 and sc < len(image[0]) - 1:
                if image[sr + 1][sc] == start and prev != "down":
                    image =  self.recursiveFill(image, sr + 1, sc, newColor, "up")
                if image[sr][sc + 1] == start and prev != "right":
                    image =  self.recursiveFill(image, sr, sc + 1, newColor, "left")
                if image[sr - 1][sc] == start and prev != "up":
                    image =  self.recursiveFill(image, sr - 1, sc, newColor, "down")
                if image[sr][sc - 1] == start and prev != "left":
                    image = self.recursiveFill(image, sr, sc - 1, newColor, "right")
            elif sc == 0:
                if image[sr + 1][sc] == start and prev != "down":
                    image = self.recursiveFill(image, sr + 1, sc, newColor, "up")
                if image[sr][sc + 1] == start and prev != "right":
                    image = self.recursiveFill(image, sr, sc + 1, newColor, "left")
                if image[sr - 1][sc] == start and prev != "up":
                    image = self.recursiveFill(image, sr - 1, sc, newColor, "down")
            else:
                if image[sr + 1][sc] == start and prev != "down":
                    image = self.recursiveFill(image, sr + 1, sc, newColor, "up")
                if image[sr - 1][sc] == start and prev != "up":
                    image = self.recursiveFill(image, sr - 1, sc, newColor, "down")
                if image[sr][sc - 1] == start and prev != "left":
                    image = self.recursiveFill(image, sr, sc - 1, newColor, "right")
        elif sr == 0:
            if sc > 0 and sc < len(image[0]) - 1:
                if image[sr + 1][sc] == start and prev != "down":
                    image = self.recursiveFill(image, sr + 1, sc, newColor, "up")
                if image[sr][sc + 1] == start and prev != "right":
                    image = self.recursiveFill(image, sr, sc + 1, newColor, "left")
                if image[sr][sc - 1] == start and prev != "left":
                    image = self.recursiveFill(image, sr, sc - 1, newColor, "right")
            elif sc == 0:
                if image[sr + 1][sc] == start and prev != "down":
                    image = self.recursiveFill(image, sr + 1, sc, newColor, "up")
                if image[sr][sc + 1] == start and prev != "right":
                    image = self.recursiveFill(image, sr, sc + 1, newColor, "left")
            else:
                if image[sr + 1][sc] == start and prev != "down":
                    image = self.recursiveFill(image, sr + 1, sc, newColor, "up")
                if image[sr][sc - 1] == start and prev != "left":
                    image = self.recursiveFill(image, sr, sc - 1, newColor, "right")
        else:
            if sc > 0 and sc < len(image[0]) - 1:
                if image[sr][sc + 1] == start and prev != "right":
                    image = self.recursiveFill(image, sr, sc + 1, newColor, "left")
                if image[sr - 1][sc] == start and prev != "up":
                    image = self.recursiveFill(image, sr - 1, sc, newColor, "down")
                if image[sr][sc - 1] == start and prev != "left":
                    image = self.recursiveFill(image, sr, sc - 1, newColor, "right")
            elif sc == 0:
                if image[sr][sc + 1] == start and prev != "right":
                    image = self.recursiveFill(image, sr, sc + 1, newColor, "left")
                if image[sr - 1][sc] == start and prev != "up":
                    image = self.recursiveFill(image, sr - 1, sc, newColor, "down")
            else:
                if image[sr - 1][sc] == start and prev != "up":
                    image = self.recursiveFill(image, sr - 1, sc, newColor, "down")
                if image[sr][sc - 1] == start and prev != "left":
                    image = self.recursiveFill(image, sr, sc - 1, newColor, "right")
        
        return image
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        return self.recursiveFill(image, sr, sc, newColor, "null")