# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:21:37 2015

@author: scholl
"""
__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150609-1200"
__status__ = "beta"
__license__ = "GPL"

import pyglet
#pyglet.lib.load_library('avbin')
#pyglet.have_avbin=True
 
class Music(object): 
    def __init__(self, fileName): 
        self.source = pyglet.media.load(fileName, streaming=False) 
        self.player = pyglet.media.Player() 
        self.player.eos_action = pyglet.media.Player.EOS_LOOP # Loops the song 
        self.player.queue(self.source) 
        self._pyglet = pyglet
    def play(self, volume = 50): 
        # self.set_volume(volume)      
        self.player.play() 
        #self._pyglet.app.run()
        
        # DEBUG 
        #print self.player.volume, "VOL" 
          
    def stop(self): 
        self.player.pause() 
        self.rewind() 
        self.exiter()
         
    def rewind(self): 
        self.player.seek(0.0) 
         
    def pause(self): 
        self.player.pause() 
         
    def unpause(self): 
        self.player.play() 
         
    def fadeout(self): 
        # TODO figure out 
        self.stop() 
         
    def is_playing(self): 
        return self.player.playing 
         
    def get_position(self): 
        return self.player.time * 1000.0 
 
    def increase_volume(self): 
        self.player.volume += 2 
  
  
    def decrease_volume(self): 
        self.player.volume -= 2 
        
    def set_volume(self, newVolume): 
        self.player.volume = newVolume 
        
    def exiter(self):
        self._pyglet.app.exit()
        #self.source.app.exit()
