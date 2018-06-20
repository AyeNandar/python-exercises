class Scene(object):

    def enter(self):
4       pass
5
6
class Engine(object):
8
9   def __init__(self, scene_map):
10      pass
11
12 def play(self):
13     pass  
14
class Death(Scene):
16
17   def enter(self):
18      pass
19
class CentralCorridor(Scene):
21
22   def enter(self):
23      pass
24
class LaserWeaponArmory(Scene):
26
27    def enter(self):
28       pass
29
class TheBridge(Scene):
31
32   def enter(self):
33       pass
34
class EscapePod(Scene):
36
37   def enter(self):
38       pass
39
40
class Map(object):
42
43    def __init__(self, start_scene):
44        pass
45
46    def next_scene(self, scene_name):
47        pass
48
49    def opening_scene(self):
50        pass
51
52
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

