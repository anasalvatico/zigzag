class bolinha():
    v = 1
    d = 20
    
    def __init__(self, x, y,limite):
        self.x = x
        self.y = y
        self.le = limite.xe
        self.ld = limite.xd
        
        
    def desenha(self):
        self.move()
        ellipse(self.x,self.y,self.d,self.d)
        
    def move(self):
        self.x += self.v
        if self.x < self.le or self.x > self.ld:
            print 'bolinha morreu'
        

    def muda(self):
        self.v *= -1

class limites():
    def __init__(self, xe, xd):
        self.xe = xe
        self.xd = xd
        
    def desenha(self):
        line(self.xe,0,self.xe,800)
        line(self.xd,0,self.xd,800)
        
        
l = limites(300,500)
b = bolinha(400,500,l)

def setup():
    size(800,600)
    
def draw():
    background(255)
    b.desenha()
    l.desenha()
    
def mousePressed():
    b.muda()
