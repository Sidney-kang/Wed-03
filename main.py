# Created by : Sidney Kang
# Created on : 27 Sept. 2017
# Created for : ICS3UR
# Wednesday Assignment - wed_04
# This scene shows 

from scene import * 
import ui

class FirstScene(Scene):
      def setup(self):
      #Add Mt blue background colour
          self.background = SpriteNode(position = self.size/2, 
                                       color = (0.61, 0.78, 0.87), 
                                       parent = self,
                                       size = self.size)
          self.school_crest = SpriteNode('./assets/sprites/MT_Crest.jpg', 
                                         parent = self, 
                                         position = self.size/2) 
      def touch_moved(self, touch):
      #Move image with your finger 
          self.school_crest.position = touch.location

# ..use when deploying app for Xcode nd the App store
main_view = ui.View() 
scene_view = SceneView(frame = main_view.bounds, flex = 'WH')
main_view.add_subview(scene_view)
scene_view.scene = FirstScene()
main_view.present(hide_title_bar = True, animated = False)
