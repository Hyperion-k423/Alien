import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings,screen) #用Ship类为ship申请了一个矩阵，大小由变量screen决定，而screen又是pygame.display.set_mode()方法定义的，里面的变量参数ai_settings又是由Settings类定义的
    bullets = Group()
    aliens =Group()
    gf.creat_fleet(ai_settings, screen, ship, aliens)
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
run_game()


