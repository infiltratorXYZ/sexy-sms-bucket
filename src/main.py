#!/usr/bin/env python3

import kivy
kivy.require('1.11.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

from jinus import autoclass


class MyApp(App):

    def build(self):
        SMS = autoclass('android/provider/Telephony/SMS_RECEIVED')
        return Label(text=SMS)


if __name__ == '__main__':
    MyApp().run()
