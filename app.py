from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader

        
class ButtonSound(App):
    def build(self):
        layout = BoxLayout(padding=15, orientation='vertical')
        btn = Button(text="Начать", background_color=[0, 1, 0, 1], on_press=self.btn_pressed)
        layout.add_widget(btn)
        return layout
    
    def btn_pressed(self, instance):
        #здесь можно сделать рандом я знаю как
        sound = SoundLoader.load('02036.mp3')
        sound.play()

if __name__ == '__main__':
    ButtonSound().run()

