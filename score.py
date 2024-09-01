import pygame
from constants import *

def display_score(screen, score):
    #set the font
    score_font = pygame.font.SysFont('Comic Sans', 30)

    #render the text with the font
    score_text = score_font.render(f"Score: {score}", False, (255,255,255))
    
    # Set the position for the score display
    text_rect = score_text.get_rect(center=(50, 50))
    
    # Blit (copy) the score to the screen
    screen.blit(score_text, text_rect)