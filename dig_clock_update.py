from graphics import *

class DigitalClock ():
    def __init__ (self, hour, minute, second, msg):
        self.hour=hour
        self.minute=minute
        self.second=second
        
        if self.hour>12:
            hour=hour-12
            pos='PM'
        else:
            pos='AM'
        self.show_time=str(hour)+':'+str(self.minute)+':'+str(self.second)+' '+pos
        self.msg=Text(Point(150,50), self.show_time)

    def update_time (self,win):
        hour = self.hour
        if self.hour>12:
            hour=hour-12
            pos='PM'
        else:
            pos='AM'
        curr_time=hour*3600+self.minute*60+self.second
        update_time=curr_time+1
        new_hour=update_time//3600
        new_minute=update_time%3600//60
        new_second=update_time%60
        hour=new_hour
        self.minute=new_minute
        self.second=new_second
        
        self.show_time=str(hour)+':'+str(self.minute)+':'+str(self.second)+' '+pos
        
        self.msg.setText(self.show_time)
        
        #        print self.show_time
        return self.show_time

    def draw_text(self, win):
         
        self.msg.setSize(30)
        self.msg.setStyle('bold')
        self.msg.setTextColor('black')        
        self.msg.draw(win)

        return self.show_time
        
    def draw_face(self,win):
        rect=Rectangle(Point(10,10),Point(290,90))
        rect.setFill('dark green')
        rect.setOutline('black')
        rect.setWidth(5)
        rect.draw(win)
        
    def tick (self, win, n):
        if n>0:
            self.update_time(win)
            
            win.after(100,self.tick,win,n-1)

new_win=GraphWin('Digital Clock', 300, 100)
clock=DigitalClock(16,50,59,'msg')
clock.draw_face(new_win)
clock.draw_text(new_win)
clock.tick(new_win,100)


##msg1=Text(Point(100,100), 'Hello world!')
##msg1.setSize(30)
##msg1.setStyle('bold')
##msg1.setTextColor('red')
##msg1.draw(new_win)

new_win.mainloop()
