from graphics import *
import math

class Clock():
    def __init__ (self, hour, minute, second):
        self.hour=hour
        self.minute=minute
        self.second=second
        self.line_hour = Line(Point(0,0), Point(0,0))
        self.line_minute = Line(Point(0,0), Point(0,0))
        self.line_second = Line(Point(0,0), Point(0,0))

    
    def update_time(self, win):
        self.second+=1
        if self.second>=60:
            self.minute+=1
            self.second=self.second-60
            if self.minute>=60:
                self.hour+=1
                self.minute=self.minute-60
    
#        print self.hour,self.minute,self.second

    def tick (self, win, n, line_hour, line_minute, line_second):
        if n>0:
            self.update_time(win)
##            print self.hour, self.minute, self.second
            self.line_hour = line_hour
            self.line_minute = line_minute
            self.line_second = line_second
            self.line_hour.undraw()
            self.line_minute.undraw()
            self.line_second.undraw()
            self.draw_time(win)
            
            win.after(100,self.tick,win,n-1, self.line_hour, self.line_minute, self.line_second)
    

##class DigitalClock (Clock):
##    def __init__(self,hour,minute,second,msg):
##        self.hour=hour
##        self.minute=minute
##        self.second=second
##        self.msg=msg
##               
##        Clock__init__(self, hour, minute, second, msg)
##        
##        if self.hour>12:
##            self.hour=self.hour-12
##            pos='PM'
##        else:
##            pos='AM'
##        self.show_time=str(self.hour)+':'+str(self.minute)+':'+str(self.second)+' '+pos
##        
##        self.msg=Text(Point(150,50), self.show_time)
##
##    def update_time (self,win):
##        curr_time=self.hour*3600+self.minute*60+self.second
##        update_time=curr_time+1
##        new_hour=update_time//3600
##        new_minute=update_time%3600//60
##        new_second=update_time%60
##        self.hour=new_hour
##        self.minute=new_minute
##        self.second=new_second
##        if self.hour>12:
##            self.hour=self.hour-12
##            pos='PM'
##        else:
##            pos='AM'
##        self.show_time=str(self.hour)+':'+str(self.minute)+':'+str(self.second)+' '+pos
##        
##        self.msg.setText(self.show_time)
##        
##        return self.show_time
##
##    def draw_text(self, win):
##         
##        self.msg.setSize(30)
##        self.msg.setStyle('bold')
##        self.msg.setTextColor('black')        
##        self.msg.draw(win)
##
##        return self.show_time
##        
##    def draw_face(self,win):
##        rect=Rectangle(Point(10,10),Point(290,90))
##        rect.setFill('dark green')
##        rect.setOutline('black')
##        rect.setWidth(5)
##        rect.draw(win)
        

class AnalogClock (Clock):
    def __init__ (self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
        #        print self.hour, self.minute, self.second
        

##        hour=self.hour
##        minute=self.minute
##        second=self.second
        
        Clock.__init__ (self, hour, minute, second)
##
##    def update_time(self, win):
##        self.second+=1
##        if self.second>=60:
##            self.minute+=1
##            self.second=self.second-60
##            if self.minute>=60:
##                self.hour+=1
##                self.minute=self.minute-60
##        return self.hour,self.minute,self.second
##        
           
    def draw_face(self,win):
        circle=Circle(Point(150,150),100)  #circle_r=100
        circle.setFill('purple')
        circle.setOutline('black')
        circle.setWidth(3)
        circle.draw(win)

    def draw_time(self,win):
##        print self.hour, self.minute, self.second          
        dx_hour=(math.sin(30*self.hour*math.pi/180))*60   #hour_r=60
        dy_hour=(math.cos(30*self.hour*math.pi/180))*60
##        print dx_hour, dy_hour
        self.line_hour=Line(Point(150,150),Point(150+dx_hour,150-dy_hour))
        self.line_hour.setFill('black')
        self.line_hour.setWidth(3)
        self.line_hour.setArrow('last')
        self.line_hour.draw(win)

        dx_minute=(math.sin(6*self.minute*math.pi/180))*90   #minute_r=90
        dy_minute=(math.cos(6*self.minute*math.pi/180))*90
        self.line_minute=Line(Point(150,150),Point(150+dx_minute,150-dy_minute))
        self.line_minute.setFill('black')
        self.line_minute.setWidth(3)
        self.line_minute.setArrow('last')
        self.line_minute.draw(win)

        dx_second=(math.sin(6*self.second*math.pi/180))*90   #second_r=90
        dy_second=(math.cos(6*self.second*math.pi/180))*90
        self.line_second=Line(Point(150,150),Point(150+dx_second,150-dy_second))
        self.line_second.setFill('black')
        self.line_second.setWidth(1)
        self.line_second.setArrow('last')
        self.line_second.draw(win)
        return self.line_hour, self.line_minute, self.line_second
    
def main1():    
    new_win=GraphWin('Digital Clock', 300, 100)
    clock=DigitalClock(4,50,59,'msg')
    clock.draw_face(new_win)
    clock.draw_text(new_win)
    clock.tick(new_win,100)

    new_win.mainloop()

def main2():    
    new_win=GraphWin('Analog Clock', 300, 300)
    clock=AnalogClock(16,59,00)
    clock.draw_face(new_win)
    line_hour, line_minute, line_second = clock.draw_time(new_win)
    clock.tick(new_win,100, line_hour, line_minute, line_second)

    new_win.mainloop()
    
#main1()
main2()
