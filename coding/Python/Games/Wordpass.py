
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle


class MyWidget(Widget):
    pass

class Wordpass(App):
    def build(self):
        self.title = "Wordpass"
        self.icon = "wordpassLogo.png"
        
        # Create a BoxLayout to hold the GridLayout and background
        layout = BoxLayout(orientation='vertical')
        
        # Create a GridLayout
        self.window = GridLayout()
        self.window.cols = 1

        # Add widgets to the GridLayout
        self.window.add_widget(Image(source="wordpassLogo.png"))
        welcome_label = Label(
            text="Welcome to Wordpass!",
            font_size=50,
            color=(45/255, 166/255, 164/255, 1),
            halign='center',
            valign='middle'
        )
        welcome_label.bind(size=welcome_label.setter('text_size'))
        self.window.add_widget(welcome_label)
        
        self.button = Button(
            text="New Password?",
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        self.window.add_widget(self.button)

        return self.window

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos



if __name__ == "__main__":
    Wordpass().run()