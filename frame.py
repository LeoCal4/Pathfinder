import pygame
import sys, time

class FrameController:

    def __init__(self, pygame, screen_size, square_size):
        self.pygame = pygame
        self.size = screen_size
        self.width = self.size[1]
        self.height = self.size[1]
        self.square_size = square_size
        self.screen = pygame.display.set_mode(self.size)
        self.rect_dict = dict()
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 200)
        self.YELLOW = (255, 255, 0)
        self.GREY = (100, 100, 100)
        self.width_in_squares = 0
        self.height_in_squares = 0

    def draw_screen(self, width_in_squares, height_in_squares):
        index = 0
        self.width_in_squares = width_in_squares
        self.height_in_squares = height_in_squares
        self.screen.fill(self.GREY)
        for y in range(0, height_in_squares):
            for x in range(0, width_in_squares):
                self.rect_dict[index] = pygame.draw.rect(self.screen, self.WHITE, (x+(self.square_size*x), y+(self.square_size*y), self.square_size, self.square_size))
                index += 1
        pygame.display.update()
        return self.rect_dict

    def color_square_by_click(self, mouse_x, mouse_y, color):
        # add some offset to the mouse position, since apparently it doesn't represent the actual tip of the mouse
        x = (mouse_x - 6) // self.square_size
        y = (mouse_y - 10) // self.square_size
        pygame.draw.rect(self.screen, color, (x*self.square_size + x, y*self.square_size + y, self.square_size, self.square_size))
        pygame.display.update()

    def color_square_by_index(self, index, color):
        if index in self.rect_dict.keys():
            rect = self.rect_dict[index]
            pygame.draw.rect(self.screen, color, (rect[0], rect[1], self.square_size, self.square_size))
            pygame.display.update()

    def get_clicked_rect_coordinates(self, mouse_x, mouse_y):
        x = ((mouse_x - 6) // self.square_size) + 1
        y = ((mouse_y - 10) // self.square_size) + 1
        index = ((y * self.width_in_squares) - (self.width_in_squares - x))-1
        print("rect clicked:", index)
        return index

    def color_shortest_path(self, shortest_path):
        for node in shortest_path:
            self.color_square_by_index(node.get_name(), self.GREEN)
            time.sleep(0.03)