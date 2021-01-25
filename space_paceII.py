import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
	#init pygame, settings and screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Space Pace II")
	#make the play button
	play_button = Button(ai_settings, screen, "Play")

	#create an instance to store game stat and create scoreboard
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	#make a ship
	ship = Ship(ai_settings, screen)
	#make a group to store bullets in
	bullets = Group()
	#make an alien
	aliens = Group()
	#create the fleet of aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)

	#setup gameloop
	while True:
		#watch for keyboard and mouse events
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()  