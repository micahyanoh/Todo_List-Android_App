from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty
#from kivy import Config
from kivy.core.window import Window
from kivy.lang import Builder
from  kivy.metrics import dp
import datetime
from datetime import date
#Config.set('graphics','height','600')
#Config.set('graphics','width','350')
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior

Window.size=(350,600)

class TodoCard(FakeRectangularElevationBehavior,MDFloatLayout):
    title=StringProperty()
    description=StringProperty()
    


class TodoApp(MDApp):
    def build(self):
        global screen_manager
        screen_manager=ScreenManager()
        screen_manager.add_widget(Builder.load_file('main.kv'))
        screen_manager.add_widget(Builder.load_file('AddTodo.kv'))
       
        return screen_manager
    def on_start(self):
        today=date.today()
        wd=date.weekday(today)
        days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        year=str(datetime.datetime.now().year)
        month=str(datetime.datetime.now().strftime("%b"))
        day=str(datetime.datetime.now().strftime("%d"))
        screen_manager.get_screen('main').date.text=f'{days[wd]} {day} {month} {year}'
        
    def on_complete(self,checkbox,value,description,bar):
        if value:
            description.text=f'[s]{description.text}[/s]'
            bar.md_bg_color=0,170/255,0,1
        else:
            remove=['[s]','[/s]']
            for i in remove:
                description.text=description.text.replace(i, '')
                bar.md_color= 1,179/255,23/255,1
    def add_todo(self,title,description):
        if title !='' and description !='' and len(title)<21 and len(description)<61:
            screen_manager.current= 'main'
            screen_manager.transition.direction= 'right'
            screen_manager.get_screen('main').todo_list.add_widget(TodoCard(title=title,description=description))
            screen_manager.get_screen('add_todo').description.text=''
        elif title =='':
           Snackbar(text='Tittle is missing!',snackbar_x='10dp',snackbar_y='10dp',size_hint_y=.08,
                    size_hint_x=(Window.width -(dp(10)*2))/Window.width, bg_color=(1,170/255,23/255,1),
                    ).open()
        elif description =='':
           Snackbar(text='Description is missing!',snackbar_x='10dp',snackbar_y='10dp',size_hint_y=.08,
                    size_hint_x=(Window.width -(dp(10)*2))/Window.width, bg_color=(1,170/255,23/255,1),
                    ).open()
        elif len(title) >21:
           Snackbar(text='Tittle lenth should be < 21!',snackbar_x='10dp',snackbar_y='10dp',size_hint_y=.08,
                    size_hint_x=(Window.width -(dp(10)*2))/Window.width, bg_color=(1,170/255,23/255,1),
                    ).open()
        elif len(description) >61:
           Snackbar(text='Tittle lenth should be < 61!',snackbar_x='10dp',snackbar_y='10dp',size_hint_y=.08,
                    size_hint_x=(Window.width -(dp(10)*2))/Window.width, bg_color=(1,170/255,23/255,1),
                    ).open()



if __name__=="__main__":
    TodoApp().run()