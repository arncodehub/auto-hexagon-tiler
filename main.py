import pygame, math, time
pygame.init()

window = pygame.display.set_mode((640, 360)) # 16:9 aspect ratio.
pygame.display.set_caption("Automated Hexagonal Tiling")
pygame.display.update()

clock = pygame.time.Clock()

class HexagonTiler:
    def __init__(self, size, layer_colors): # Create the class before using the method!
        self.size = size
        self.layer_colors = layer_colors
    
    def draw_hexagon(self, window, color, topleftX, topleftY, dX, dY):
        points = []
        points.append((topleftX, topleftY))
        points.append((topleftX+self.size, topleftY))
        points.append((topleftX+self.size+dX, topleftY-dY))
        points.append((topleftX+self.size, topleftY-dY*2))
        points.append((topleftX, topleftY-dY*2))
        points.append((topleftX-dX, topleftY-dY))
        pygame.draw.polygon(window, color, points)

    def delay(self, seconds=0):
        pygame.display.update()
        time.sleep(seconds)

    def draw_pattern(self, surface, delay): # Call this function!
        if delay: delay = 0.5
        S = math.sin(math.radians(150)) * self.size
        C = math.cos(math.radians(150)) * self.size
        rS, rC = round(S), round(C)
        for layer in range(len(self.layer_colors)-1, -1, -1):
            tlX, tlY = 320-S, 180-C-self.size*1.5
            tlY += 2*layer*C
            self.draw_hexagon(surface, self.layer_colors[layer], tlX, tlY, S, C)
            self.delay(delay)
            for i in range(layer):
                tlX += 3*S
                tlY -= C
                self.draw_hexagon(surface, self.layer_colors[layer], tlX, tlY, S, C)
                self.delay(delay)
            for i in range(layer):
                tlY -= 2*C
                self.draw_hexagon(surface, self.layer_colors[layer], tlX, tlY, S, C)
                self.delay(delay)
            for i in range(layer):
                tlX -= 3*S
                tlY -= C
                self.draw_hexagon(surface, self.layer_colors[layer], tlX, tlY, S, C)
                self.delay(delay)                
            for i in range(layer):
                tlX -= 3*S
                tlY += C
                self.draw_hexagon(surface, self.layer_colors[layer], tlX, tlY, S, C)
                self.delay(delay)                
            for i in range(layer):
                tlY += 2*C
                self.draw_hexagon(surface, self.layer_colors[layer], tlX, tlY, S, C)
                self.delay(delay)                
            for i in range(layer-1):
                tlX += 3*S
                tlY += C
                self.draw_hexagon(surface, self.layer_colors[layer], tlX, tlY, S, C)
                self.delay(delay)                

# BLOCK: INSERT CODE BELOW v
tiler = HexagonTiler(20, [(0, 0, 255), (255, 0, 0), (255, 255, 0), (0, 255, 0)])
# BLOCK: INSERT CODE ABOVE ^

def main():
    run = True
    window.fill((0, 0, 0))
    # BLOCK: INSERT CODE BELOW v
    tiler.draw_pattern(window, False)
    # BLOCK: INSERT CODE ABOVE ^
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
