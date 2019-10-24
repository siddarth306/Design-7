# Time Complexity: O(n) where n is the size of the snake which can be at max width*height size
# Space Complexity: O(n) where n is the size of the snake which can be at max width*height size
# Approach: Save the snake's body coordinates in a queue (initially with size 1)
#			Check if the next coordinate will cause a collision with itself or with one of the boundaries. If so return -1
#			Check if the next coordinate is a food item, increase the allowed size by 1. 
#			Append coordinate to the snake's body. If the size of the body == allowed_size, pop left.
#			Return the size of the snake - 1 as the result.
class SnakeGame:

    class Snake:
        def __init__(self):
            self.size = 1
            self.body_coord = [(0,0)]
            
        def add_point(self, coord):
            if len(self.body_coord) == self.size:
                self.body_coord.pop(0)
            self.body_coord.append(coord)
            
        def inc_size(self):
            self.size += 1
            
        def check_collision(self, coord):
            if coord in self.body_coord[1:]:
                return True
            return False

        def get_head(self):
            return self.body_coord[-1]
        
    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.snake = self.Snake()
        self.width = width
        self.height = height
        self.food = food
        self.direction_map = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}
        
    def check_boundary_collision(self, coord):
        return 0 <= coord[0] < self.height and 0 <= coord[1] < self.width

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        head = self.snake.get_head()
        next_direction = self.direction_map[direction]
        next_coord = (head[0] + next_direction[0], head[1] + next_direction[1])
        if (self.check_boundary_collision(next_coord)) and (not self.snake.check_collision(next_coord)):
            if len(self.food) > 0 and tuple(self.food[0]) == next_coord:
                self.food.pop(0)
                self.snake.inc_size()
                
            self.snake.add_point(next_coord)
            return self.snake.size -1
        else:
            return -1
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)