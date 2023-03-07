import pygame

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Set the caption of the window
pygame.display.set_caption("Testing")

# Define the font for the buttons and the title
font = pygame.font.Font("Times New Roman", 72)

# Define the text for the buttons and the title
title_text = font.render("Testing", True, (255, 255, 255))
start_text = font.render("Start", True, (255, 255, 255))
exit_text = font.render("Exit", True, (255, 255, 255))

# Define the colors for the buttons
button_color = (0, 0, 255)
button_border_color = (255, 255, 255)

# Create the button surfaces
button_width = max(start_text.get_width(), exit_text.get_width()) + 40
button_height = start_text.get_height() + 40
button_radius = 10

start_button_surf = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
pygame.draw.rect(start_button_surf, button_border_color, pygame.Rect((0, 0), (button_width, button_height)), border_radius=button_radius)
pygame.draw.rect(start_button_surf, button_color, pygame.Rect((2, 2), (button_width - 4, button_height - 4)), border_radius=button_radius)
start_button_surf.blit(start_text, ((button_width - start_text.get_width()) // 2, (button_height - start_text.get_height()) // 2))

exit_button_surf = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
pygame.draw.rect(exit_button_surf, button_border_color, pygame.Rect((0, 0), (button_width, button_height)), border_radius=button_radius)
pygame.draw.rect(exit_button_surf, button_color, pygame.Rect((2, 2), (button_width - 4, button_height - 4)), border_radius=button_radius)
exit_button_surf.blit(exit_text, ((button_width - exit_text.get_width()) // 2, (button_height - exit_text.get_height()) // 2))

# Set the position of the title and the buttons
title_pos = ((screen.get_width() - title_text.get_width()) // 2, (screen.get_height() - title_text.get_height()) // 2)
start_button_pos = (screen.get_width() - button_width - 40, screen.get_height() - button_height - 40)
exit_button_pos = (screen.get_width() - button_width - 40, screen.get_height() - (2 * button_height) - 60)

# Draw the title and the buttons
screen.blit(title_text, title_pos)
screen.blit(start_button_surf, start_button_pos)
screen.blit(exit_button_surf, exit_button_pos)

# Update the display
pygame.display.update()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if start_button_surf.get_rect(topleft=start_button_pos).collidepoint(event.pos):
                # Start the game here
                pass
            elif exit_button_surf.get_rect(topleft=exit_button_pos).collidepoint(event.pos):
                pygame.quit()
                quit()
