import pyglet

snd = pyglet.media.load('music/Moon_veil_-_01_-_Mantilla.mp3')
looper = pyglet.media.SourceGroup(snd.audio_format, None)
looper.loop = False
looper.queue(snd)
p = pyglet.media.Player()
p.queue(looper)
p.play()