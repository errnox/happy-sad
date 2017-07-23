import math
import random

import pyglet


class Game(pyglet.window.Window):
  def __init__(self, width=700, height=500):
    super(Game, self).__init__(width=width, height=height)

    pyglet.resource.path = ['./images']
    pyglet.resource.reindex()
    self.happy_image = pyglet.resource.image('happy.png')
    self.sad_image = pyglet.resource.image('sad.png')
    self.unsure_image = pyglet.resource.image('unsure.png')
    self.recenter_image(self.happy_image)
    self.recenter_image(self.sad_image)
    self.recenter_image(self.unsure_image)
    self.happy_sprite = pyglet.sprite.Sprite(
        img=self.happy_image, x=self.width / 3, y = self.height / 3)
    self.sad_sprite = pyglet.sprite.Sprite(
        img=self.sad_image, x=self.width / 4, y = self.height / 4)
    self.unsure_sprite = pyglet.sprite.Sprite(
        img=self.unsure_image, x=self.width / 5, y = self.height / 5)

    self.sprites = []
    self.sprites.append(self.happy_sprite)
    self.sprites.append(self.sad_sprite)
    self.sprites.append(self.unsure_sprite)

    self.main_label = pyglet.text.Label(
        text='Happy Sad', x=self.width/2, y=self.height/2,
        anchor_x='center', anchor_y='center')
    self.theta = 0.0

  def run(self):
      pyglet.app.run()

  def recenter_image(self, image):
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

  def update(self):
    if self.theta > 0:
        self.theta -= 1 * 0.1
    else:
        self.theta = 2 * math.pi
    self.main_label.x = self.width/2 + math.cos(self.theta) * 30
    self.main_label.y = self.height/2 + math.sin(self.theta) * 30

    self.happy_sprite.scale += random.randint(-2, 2) * 0.05
    self.happy_sprite.rotation += random.randint(-1, 1) * 3

    self.sad_sprite.x += 1 * 1.3
    self.sad_sprite.y += math.sin(random.randint(-1, 1) * 2)
    if self.sad_sprite.x < 0:
        self.sad_sprite.x = self.width
    elif self.sad_sprite.x > self.width:
        self.sad_sprite.x = 0
    if self.sad_sprite.y < 0:
        self.sad_sprite.y = self.height
    elif self.sad_sprite.y > self.height:
        self.sad_sprite.y = 0

  def on_draw(self):
    self.clear()
    self.update()
    self.main_label.draw()
    for sprite in self.sprites:
      sprite.draw()

  def on_key_press(self, symbol, modifiers):
    if symbol == pyglet.window.key.PLUS:
      self.happy_sprite.scale += 3
    elif symbol == pyglet.window.key.MINUS:
      self.happy_sprite.scale -= 3
    elif symbol == pyglet.window.key.UP:
      self.unsure_sprite.y += 20
    elif symbol == pyglet.window.key.DOWN:
      self.unsure_sprite.y -= 20
    elif symbol == pyglet.window.key.RIGHT:
      self.unsure_sprite.x += 20
    elif symbol == pyglet.window.key.LEFT:
      self.unsure_sprite.x -= 20


if __name__ == '__main__':
    game = Game()
    game.run()
