#功能：测试
#说明: Python版本 3.13.5

import pygame
import sys
import random
import os

# 设置窗口尺寸
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAME_RATE = 60
SPEED = 3
DIRECTION_CHANGE_PROB = 0.02  # 方向改变概率
BG_COLOR = (30, 144, 255)     # 背景颜色
FPS_COLOR = (255, 255, 255)   # FPS文本颜色

class GameSprite:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed_x = SPEED
        self.speed_y = SPEED
        self.reset_position()

    def reset_position(self):
        """重置精灵位置到屏幕中央"""
        self.rect.x = WINDOW_WIDTH // 2
        self.rect.y = WINDOW_HEIGHT // 2

    def update(self):
        """更新精灵位置并处理碰撞"""
        self.move()
        self.handle_collision()
        self.random_direction_change()

    def move(self):
        """移动精灵"""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def handle_collision(self):
        """处理边界碰撞"""
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.speed_y = -self.speed_y

    def random_direction_change(self):
        """随机改变方向"""
        if random.random() < DIRECTION_CHANGE_PROB:
            self.speed_x = random.choice([-SPEED, SPEED])
            self.speed_y = random.choice([-SPEED, SPEED])

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('移动的图片')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.sprite = GameSprite('file//test_image.png')
        self.running = True

    def handle_events(self):
        """处理游戏事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """更新游戏状态"""
        self.clock.tick(FRAME_RATE)
        self.sprite.update()

    def draw(self):
        """绘制游戏画面"""
        self.screen.fill(BG_COLOR)
        self.screen.blit(self.sprite.image, self.sprite.rect)
        self.draw_fps()
        pygame.display.flip()

    def draw_fps(self):
        """显示帧率"""
        fps_text = self.font.render(f"FPS: {int(self.clock.get_fps())}", True, FPS_COLOR)
        self.screen.blit(fps_text, (10, 10))

    def run(self):
        """运行游戏主循环"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
        self.quit()

    def quit(self):
        """退出游戏"""
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
