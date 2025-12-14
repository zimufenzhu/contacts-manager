from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window

# 设置窗口大小（仅用于开发测试，打包为APK时会自动适应屏幕）
Window.size = (360, 640)

# 导入各个屏幕界面
from screens.main_screen import MainScreen
from screens.contact_list_screen import ContactListScreen
from screens.contact_detail_screen import ContactDetailScreen
from screens.contact_edit_screen import ContactEditScreen
from screens.settings_screen import SettingsScreen


class ContactManagerApp(App):
    def build(self):
        # 创建屏幕管理器
        sm = ScreenManager()
        
        # 添加各个屏幕
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(ContactListScreen(name='contact_list'))
        sm.add_widget(ContactDetailScreen(name='contact_detail'))
        sm.add_widget(ContactEditScreen(name='contact_edit'))
        sm.add_widget(SettingsScreen(name='settings'))
        
        return sm


if __name__ == '__main__':
    ContactManagerApp().run()