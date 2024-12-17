import kivy 
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 
from kivy.uix.image import Image 
from kivy.uix.progressbar import ProgressBar 
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup

class CharacterSheet(GridLayout): 
    def __init__(self, **kwargs): 
        super(CharacterSheet, self).__init__(cols=2, **kwargs)
        
        # Name field
        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False, readonly=True)
        self.add_widget(self.name)

        # Experience Points
        self.add_widget(Label(text="Experience Points: "))
        self.experience_points = TextInput(multiline=False, readonly=True)
        self.add_widget(self.experience_points)

        # Level Progress
        self.add_widget(Label(text="Level Progress: "))
        self.level_progress = ProgressBar(max=100)
        self.add_widget(self.level_progress)

        # Impulse Points
        self.add_widget(Label(text="Impulse Points: "))
        self.impulse_points = TextInput(multiline=False, readonly=True)
        self.add_widget(self.impulse_points)

        # Import Avatar Button
        self.import_avatar_button = Button(text="Import Avatar")
        self.import_avatar_button.bind(on_press=self.import_avatar)
        self.add_widget(self.import_avatar_button)

        # Avatar Display
        self.avatar = Image()
        self.add_widget(self.avatar)

    def import_avatar(self, instance):
        file_chooser = FileChooserListView()
        popup = Popup(title="Select an Avatar File",
                      content=file_chooser,
                      size_hint=(0.9, 0.9))

        # Function to load the selected file
        def load_file(*args):
            if not file_chooser.selection:
                error_popup = Popup(
                    title="Error",
                    content=Label(text="No file was selected"),
                    size_hint=(None, None),
                    size=(400, 200)
                )
                error_popup.open()
                return

            file_path = file_chooser.selection[0]
            self.avatar.source = file_path
            popup.dismiss()

        file_chooser.bind(on_submit=lambda _, selection, __: load_file())
        popup.open()

    def calculate_level(self):
        experience = int(self.experience_points.text)
        impulse = int(self.impulse_points.text)
        level = experience // 100 + impulse // 10
        self.level_progress.value = level


class CharacterSheetApp(App): 
    def build(self): 
        return CharacterSheet()


if __name__ == "__main__":
    CharacterSheetApp().run()
