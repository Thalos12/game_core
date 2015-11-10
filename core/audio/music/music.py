import pyglet

pyglet.options['audio'] = ('openal', 'silent')

explosion = pyglet.media.load('music1.mp3', streaming=False)
explosion.play()

