import os
import time
import shutil

from kivy.clock import mainthread
from kivy.lang import Builder
from kivy_garden.mapview import MapMarker, MarkerMapLayer
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar

import request_permissions_api
from plyer import gps
from kivy.utils import platform

APP_FOLDER = os.path.dirname(os.path.abspath(__file__))
ASSETS_FOLDER = os.path.join(APP_FOLDER, 'assets')


class MainScreen(MDScreen):
    pass


class MapViewApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lat = 0
        self.lon = 0
        self.map = None

    def build(self):
        try:
            gps.configure(on_location=self.on_location,
                          on_status=self.on_status)
        except NotImplementedError:
            import traceback
            traceback.print_exc()

        if platform == "android":
            request_permissions_api.request_android_permissions()

        return Builder.load_file('main.kv')

    def get_location(self):
        self.clear_map_from_markers()
        gps.start()
        time.sleep(3)
        if self.lat and self.lon:
            marker = MapMarker(source=os.path.join(ASSETS_FOLDER, 'map_marker64x64.png'), lat=self.lat, lon=self.lon)
            self.map.add_marker(marker)
            time.sleep(0.5)
            self.map.center_on(self.lat, self.lon)
            time.sleep(0.25)
            if self.map.zoom < 10:
                self.map.zoom = 10
        else:
            Snackbar(text='Something went wrong, try again...').show()

    @mainthread
    def on_location(self, **kwargs):
        self.lat = kwargs.get("lat")
        self.lon = kwargs.get("lon")

    @mainthread
    def on_status(self, stype, status):
        pass

    def on_start(self):
        self.map = self.root.ids.main_screen.ids.map_id
        gps.start()
        super().on_start()

    def on_stop(self):
        self.delete_cache()
        gps.stop()
        super().on_stop()

    def on_pause(self):
        gps.stop()
        return super().on_pause()

    def on_resume(self):
        gps.start()
        super().on_resume()

    def clear_map_from_markers(self):
        for layer in self.map.children:
            if isinstance(layer, MarkerMapLayer):
                for marker in layer.children:
                    self.map.remove_marker(marker)

    @staticmethod
    def delete_cache():
        try:
            shutil.rmtree(os.path.join(APP_FOLDER, 'cache'))
        except FileNotFoundError:
            pass


MapViewApp().run()
