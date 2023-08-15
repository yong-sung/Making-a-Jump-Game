import pygame
import sys

FPS = 60
MAX_WIDTH = 600
MAX_HEIGHT = 400

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

class Player():
    def __init__(self, x, y): # 플레이어의 초기 위치('x', 'y')와 점프 상태 초기화
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 10

    def draw(self):
        return pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 40, 40)) # 파란색 사각형 그리기

    # 플레이어의 점프 동작을 구현한 메서드
    def jump(self): # 'isJump' 상태와 'jumpCount'를 이용해 플레이어의 y 좌표를 변경
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount**2 * 0.7 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

class Enemy():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def draw(self):
        return pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 20, 40))
    
    def move(self,speed): # 적의 x좌표 속도('speed')에 따라 변경
        self.x = self.x - speed
        if self.x <= 0:
            self.x = MAX_WIDTH

player = Player(50, MAX_HEIGHT - 40)
enemy = Enemy(MAX_WIDTH, MAX_HEIGHT - 40)

def main():
    
    speed = 7
    
    while True: # 무한 루프 안에서 게임 동작이 반복 실행
        for event in pygame.event.get(): # 발생한 이벤트(키 입력, 종료 등)를 가져옴
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.isJump = True
                    
        clock.tick(FPS) 
        screen.fill((255, 255, 255))
        
        player_rect = player.draw()
        player.jump()
        
        enemy_rect = enemy.draw()
        enemy.move(speed)
        speed = speed + 0.01
        
        if player_rect.colliderect(enemy_rect):
            print("충돌")
            pygame.quit()
            sys.exit()
        
        pygame.display.update()

if __name__ == '__main__': #'pygame'을 초기화하고 'main()'함수를 실행해 게임을 시작
    main()