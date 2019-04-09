import pyglet
from pyglet.gl import *

# Optional audio outputs (Linux examples):
# pyglet.options['audio'] = ('alsa', 'openal', 'silent')
key = pyglet.window.key

class Spr(pyglet.sprite.Sprite):
    def __init__(self, texture, x=None, y=None, moveable=True):
        self.texture = pyglet.image.load(texture)
        super(Spr, self).__init__(self.texture)
        self.moveable = moveable

    def move(self, x, y):
        if self.moveable:
            self.x += x
            self.y += y

class main(pyglet.window.Window):
    def __init__ (self):
        super(main, self).__init__(800, 800, fullscreen = False)
        self.x, self.y = 0, 0

        self.bg = pyglet.sprite.Sprite(pyglet.image.load('background.jpg'))
        self.sprites = {'SuperMario' : Spr('mario.jpg')}
        self.player = pyglet.media.Player()
        self.alive = 1

    def on_draw(self):
        self.render()

    def on_close(self):
        self.alive = 0

    def on_key_press(self, symbol, modifiers):
        if symbol in (key.LEFT, key.BACKSPACE):
            self.idx -= 1
            if self.idx < 0:
                self.idx = len(self.units) - 1
        elif symbol in (key.RIGHT, key.ENTER):
            self.idx += 1
            if self.idx > len(self.units) - 1:
                self.idx = 0

        if symbol in (key.LEFT, key.RIGHT, key.ENTER, key.BACKSPACE):
            children = self.get_children()
            if self.item in children:
                self.remove(self.item)
            if self.selected_item in children:
                self.remove(self.selected_item)

            self._update_selected_unit()
            self.draw()
            self.callback_func(self.idx)
            return True 

    def render(self):
        self.clear()
        self.bg.draw()

        # self.sprites is a dictionary where you store sprites
        # to be rendered, if you have any.
        for sprite_name, sprite in self.sprites.items():
            sprite.draw()

        self.flip()

    def run(self):
        while self.alive == 1:
            self.render()

            # -----------> This is key <----------
            # This is what replaces pyglet.app.run()
            # but is required for the GUI to not freeze
            #
            event = self.dispatch_events()
        self.player.delete() # Free resources. (Not really needed but as an example)

x = main()
x.run()