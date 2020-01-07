import pathfinding_algorithms, graph, frame
import pygame, sys
pygame.init()

LEFT_MOUSE_BUTTON = 1
RIGHT_MOUSE_BUTTON = 3

def game_loop(frame, graph, pathfinder):
    frame.draw_screen(square_size_width, square_size_heigth)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pathfinder.breadth_first_search(graph.get_first_node(), graph.get_last_node())
                if event.key == pygame.K_w:
                    pathfinder.depth_first_search(graph.get_first_node(), graph.get_last_node())
                if event.key == pygame.K_r:
                    frame.draw_screen(square_size_width, square_size_heigth)
                    graph.unlock_all_nodes()
            elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    clicked_rect_index = frame.get_clicked_rect_coordinates(mouse_x, mouse_y) 
                    if event.button == LEFT_MOUSE_BUTTON:
                        frame.color_square_by_index(clicked_rect_index, frame.RED)
                        graph.set_blocked_node(clicked_rect_index, True)
                    elif event.button == RIGHT_MOUSE_BUTTON:
                        frame.color_square_by_index(clicked_rect_index, frame.WHITE)
                        graph.set_blocked_node(clicked_rect_index, False)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = event
                while event.type is not pygame.MOUSEBUTTONUP:
                    for event in pygame.event.get():
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        clicked_rect_index = frame.get_clicked_rect_coordinates(mouse_x, mouse_y) 
                        if click.button == LEFT_MOUSE_BUTTON:
                            frame.color_square_by_index(clicked_rect_index, frame.RED)
                            graph.set_blocked_node(clicked_rect_index, True)
                        elif click.button == RIGHT_MOUSE_BUTTON:
                            frame.color_square_by_index(clicked_rect_index, frame.WHITE)
                            graph.set_blocked_node(clicked_rect_index, False)
square_size_width = 20
square_size_heigth = 15

frame = frame.FrameController(pygame, (720, 720), 30)
graph = graph.create_squared_graph(square_size_heigth, square_size_width)
pathfinder = pathfinding_algorithms.Pathfinder(frame, graph)
game_loop(frame, graph, pathfinder)