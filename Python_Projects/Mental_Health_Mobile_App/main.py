import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MoodTrackerApp(App):
    def build(self):
        # create a vertical box layout
        layout = BoxLayout(orientation='vertical')

        # add a label to the layout
        label = Label(text='How are you feeling today?')
        layout.add_widget(label)

        # create a horizontal box layout for the buttons
        button_layout = BoxLayout(orientation='horizontal')

        # create the buttons and add them to the button layout
        button1 = Button(text='Happy')
        button_layout.add_widget(button1)

        button2 = Button(text='Neutral')
        button_layout.add_widget(button2)

        button3 = Button(text='Sad')
        button_layout.add_widget(button3)

        # add the button layout to the main layout
        layout.add_widget(button_layout)

        return layout

if __name__ == '__main__':
    MoodTrackerApp().run()
