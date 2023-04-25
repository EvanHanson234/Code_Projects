import calendar
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

from kivy.lang import Builder
Builder.load_file('style.kv')

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 32
        self.rows = 13
        self.spacing = 1

        # Add month labels to the top of the grid
        self.add_widget(Button(text=""))
        for month in range(1, 13):
            self.add_widget(Button(text=calendar.month_abbr[month]))

        # Add day labels to the left of the grid
        for day in range(1, 32):
            self.add_widget(Button(text=str(day)))

            # Add rating buttons for each day of the year
            for month in range(1, 13):
                rating_btn = Button(text="", background_color=(0, 0, 0, 0), background_normal="")
                rating_btn.bind(on_press=self.on_button_click)
                self.add_widget(rating_btn)
                
    def on_button_click(self, instance):
        # Change the color of the button when clicked
        if instance.background_color == (1, 1, 0, 1):
            instance.background_color = (0, 0, 0, 0)
        else:
            instance.background_color = (1, 1, 0, 1)

class MyBox(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBox, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 100
        self.spacing = 100
        self.add_widget(MyGrid())

class MyApp(App):
    def build(self):
        # Set the window size to match the size of the grid
        Window.size = (640, 704)
        return MyBox()

if __name__ == "__main__":
    MyApp().run()
