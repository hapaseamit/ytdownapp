from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


class YTDownApp(MDApp):
    def build(self):
        myscreen = MDScreen()
        btn_flat = MDRectangleFlatButton(
            text="Click Me!",
            pos_hint={
                "center_x": 0.5,
                "center_y": 0.5,
            },
        )
        label = MDLabel(
            text="Hello World!",
            halign="left",
            theme_text_color="Error",
        )
        myscreen.add_widget(btn_flat)
        myscreen.add_widget(label)
        return myscreen


YTDownApp().run()
