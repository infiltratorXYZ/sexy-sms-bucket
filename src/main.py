#!/usr/bin/env python3
__version__ = '0.1.0' # 0.1.0-alpha

import kivy
kivy.require('1.11.1')

from kivy.app import App

from plyer import sms, vibrator
from android.permissions import check_permission, request_permissions, Permission # unresolved import is OK

# UI imports
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class SendTestSMS(GridLayout):
    message = "TEST MESSAGE (kivy app)"

    def __init__(self, **kwargs):
        super(SendTestSMS, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='test SMS, provide number'))

        self.recipient = TextInput(multiline=False)
        self.add_widget(self.recipient)

        self.sendButton = Button(text="send test SMS", font_size=14)
        self.sendButton.bind(on_press=self.send)
        self.add_widget(self.sendButton)

    def send(self, _):
        print("[myDEBUG] Button pressed")
        if not check_permission('android.permission.SEND_SMS'):
            request_permissions([Permission.SEND_SMS])

        sms.send(self.recipient.text, self.message)
        vibrator.vibrate(0.3)
        
class SSBApp(App):

    def build(self):
        vibrator.vibrate(0.3)
        return SendTestSMS()


if __name__ == '__main__':
    SSBApp().run()
