from random import randint

class bolinha():
    v = 1
    d = 20
    
    def __init__(self, x, y,limite):
        self.x = x
        self.y = y
        self.novolimite(limite)
        
    def novolimite(self, limite):
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
        
    

class limite():
    def __init__(self, xe, xd, y):
        self.xe = xe
        self.xd = xd
        self.y = y
        
    def desenha(self):
        stroke(205,100,80)
        line(self.xe,self.y,self.xd,self.y)

class plataforma():
    limites = []
    
    def __init__(self,xe,xd):
        dir = -1
        tam = 0
        for n in range(600):
            self.limites.append(limite(xe,xd, n))
            xe += dir
            xd += dir
            tam -= 1
            
            if tam <= 0:
                tam = randint(50,150)
                dir *= -1
            
    def desenha(self):
        for l in self.limites:
            l.y += 1
            if l.y == b.y:
                b.le = l.xe
                b.ld = l.xd
            l.desenha()

p = plataforma(300,450)
b = bolinha(400,500, plataforma.limites[500])

def setup():
    size(800,600)
    
def draw():
    background(255)
    p.desenha()
    b.desenha()
    stroke(0)
    line(b.le,b.y-10,b.le,b.y+10)
    line(b.ld,b.y-10,b.ld,b.y+10)
      
      
def mousePressed():
    b.muda()