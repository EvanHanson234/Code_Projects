import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 13
        self.rows = 32
        self.spacing = 1
        
        # Add month labels to the top of the grid
        self.add_widget(Button(text=""))
        self.add_widget(Button(text="Jan"))
        self.add_widget(Button(text="Feb"))
        self.add_widget(Button(text="Mar"))
        self.add_widget(Button(text="Apr"))
        self.add_widget(Button(text="May"))
        self.add_widget(Button(text="Jun"))
        self.add_widget(Button(text="Jul"))
        self.add_widget(Button(text="Aug"))
        self.add_widget(Button(text="Sep"))
        self.add_widget(Button(text="Oct"))
        self.add_widget(Button(text="Nov"))
        self.add_widget(Button(text="Dec"))
        
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
