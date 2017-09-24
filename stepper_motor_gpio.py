# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# Iniciando os pinos como saída #
GPIO.setup(11, GPIO.OUT) # P0.1
GPIO.setup(15, GPIO.OUT) # P0.2
GPIO.setup(12, GPIO.OUT) # P0.3
GPIO.setup(16, GPIO.OUT) # P0.4

class Motor_Passo:

    def __init__(self, passo, s = 'h', init = 0):
        self.passo = passo
        self.s = s
        self.init = init

    def gpio(self, P01, P02, P03, P04):
        GPIO.output(11, P01)
        GPIO.output(15, P02)
        GPIO.output(12, P03)
        GPIO.output(16, P04)
        

    def sequence_gpio(self):
        return [[True, False, False, False],
                [False, True, False, False],
                [False, False, True, False],
                [False, False, False, True]]        

    def sentido(self):
        seq = self.sequence_gpio()
        if self.s == 'h':
            return seq
        else:
            seq.reverse()
            return seq

    def run(self):
        Seq = self.sentido()
        for i in range(self.init, self.passo + self.init):            
            p01, p02, p03, p04 = Seq[i%4]
##            print p01, p02, p03, p04
            self.gpio(p01, p02, p03, p04)
            time.sleep(0.05)
        return i%4

def stop():
    GPIO.output(11, False)
    GPIO.output(15, False)
    GPIO.output(12, False)
    GPIO.output(16, False)

def cond(t, i, j, k, s):
    if i != 0:
        if s == 'h':
            j = 0
            if ( ((t == 0) or (t == 2)) and (k == 0) ):
                k = 1
                return t, j, k
            elif k != 0:                
                t += 1
                return t, j, k
            else:
                t += 2
                k = 1
                return t, j, k
        else:
            k = 0
            if ( ((t == 0) or (t == 2)) and j == 0):
                j = 1
                return t, j, k
            elif j != 0:
                t += 1
                return t, j, k
            else:
                t += 2
                j = 1
                return t, j, k
    else:
        return t, j, k

##t = 0
##i = 0
##j = 1
##k = 1
##
##print 'Programa motor de passo'
##print 'Digite o numero de passos e o sentido, caso queira sair digite e'
##print 'Obs.: h -> sentido horario e a -> sentido anti-horario \n'
##
##while True:
##    x = raw_input('Digite o numero de passos e sentido: ')
##    x = x.split()
##    if ( (x[0] == 'e') or (x[0] == 'exit') ):
##        stop()        
##        break
##    passo, s = int(x[0]), x[1]
##    t, j, k = cond(t, i, j, k, s) 
##    i = 1
##    motor = Motor_Passo(passo, s, t)
##    t = motor.run()
##    #print t




    
