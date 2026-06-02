import time
import datetime
import pygame

def set_alarm(alarm_time):
    
    sound_file = "project stuff/alarm_music.mpeg"
    is_running = True
    
    while is_running :
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)
        
        if current_time == alarm_time :
            print("wake up!!!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy() :
               time.sleep(1) 
               
               
            is_running = False    
 
if __name__ == '__main__' :
    alarm_time = input("Enter the time you want to wakeup ( HH:MM:SS) : ")
    set_alarm(alarm_time)