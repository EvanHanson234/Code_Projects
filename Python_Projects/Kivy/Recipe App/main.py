from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class recipe(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # add widgets to window

        # title widget
        self.window.add_widget(Label(
                        text="What are we cookin?",
                        font_size=100,
                        color='#00FFCE',
                        baccolor='#00FFCE'
                        ))
        
        # BUTTONS start --------------------------------------------------\
        # button 1 (Apps)
        self.button1 = Button(
                        text="Apps",
                        size_hint=(None, None),
                        size=(140, 50),
                        pos_hint={'x': 0},
                        bold=True,
                        background_color='#00FFCE'
                        )

        self.window.add_widget(self.button1)
        self.button1.bind(on_press=self.callback)
        
        # button 2 (Mains)
        self.button2 = Button(
                        text="Mains",
                        size_hint=(None, None),
                        size=(140, 50),
                        pos_hint={'x': 0},
                        bold=True,
                        background_color='#00FFCE',
                        )
        self.window.add_widget(self.button2)
        self.button2.bind(on_press=self.callback)
        
        # button 3 (Sides)
        self.button3 = Button(
                        text="Sides",
                        size_hint=(None, None),
                        size=(140, 50),
                        pos_hint={'x': 0},
                        bold=True,
                        background_color='#00FFCE',
                        )
        self.window.add_widget(self.button3)
        self.button3.bind(on_press=self.callback)

        # button 4 (Desserts)
        self.button4 = Button(
                        text="Desserts",
                        size_hint=(None, None),
                        size=(140, 50),
                        pos_hint={'x': 0},
                        bold=True,
                        background_color='#00FFCE',
                        )
        self.window.add_widget(self.button4)
        self.button4.bind(on_press=self.callback)

        # button 5 (Drinks)
        self.button5 = Button(
                        text="Drinks",
                        size_hint=(None, None),
                        size=(140, 50),
                        pos_hint={'x': 0},
                        bold=True,
                        background_color='#00FFCE',
                        )
        self.window.add_widget(self.button5)
        self.button5.bind(on_press=self.callback)

        # BUTTONS end --------------------------------------------------/

        # image widget
        #self.window.add_widget(Image(source="irish.png"))

        # label widget
        self.greeting = Label(
                        text="What's your name?", 
                        font_size=18,
                        color='#00FFCE'
                        )
        self.window.add_widget(self.greeting)

        # button widget
        #self.button = Button(
         #               text="GREET", 
          #              size_hint=(1, 0.5),
          #             bold=True, 
          #              background_color='#00FFCE',
          #              )
        #self.button.bind(on_press=self.callback)
        

        return self.window

    def callback(self, instance):
        self.greeting.text = "Hello " + self.user.text + "!"
    
if __name__ == '__main__':
    recipe().run()