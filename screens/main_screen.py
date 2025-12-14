from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from utils.contact_manager import ContactManager


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.contact_manager = ContactManager()


# 加载KV文件
Builder.load_string('''
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        MDToolbar:
            title: "联系人管理"
            elevation: 10
            left_action_items: [["menu", lambda x: None]]
            right_action_items: [["magnify", lambda x: None]]
            
        MDBottomNavigation:
            panel_color: .2, .2, .2, 1
            
            MDBottomNavigationItem:
                name: 'screen1'
                text: '联系人'
                icon: 'account-multiple'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: "10dp"
                    spacing: "10dp"
                    
                    MDTextField:
                        id: search_field
                        hint_text: "搜索联系人..."
                        icon_right: "magnify"
                        icon_right_color: app.theme_cls.primary_color
                        
                    MDCard:
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "160dp", "100dp"
                        pos_hint: {"center_x": .5}
                        
                        MDLabel:
                            text: "全部联系人"
                            theme_text_color: "Primary"
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            id: contact_count_label
                            text: "0 个联系人"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDRaisedButton:
                            text: "查看全部"
                            size_hint: None, None
                            size: "120dp", "30dp"
                            pos_hint: {"center_x": .5}
                            on_press: root.manager.current = 'contact_list'
                        
                    MDCard:
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "160dp", "100dp"
                        pos_hint: {"center_x": .5}
                        
                        MDLabel:
                            text: "最近添加"
                            theme_text_color: "Primary"
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "暂无数据"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDRaisedButton:
                            text: "查看详情"
                            size_hint: None, None
                            size: "120dp", "30dp"
                            pos_hint: {"center_x": .5}
                            on_press: root.manager.current = 'contact_list'
                        
            MDBottomNavigationItem:
                name: 'screen2'
                text: '收藏'
                icon: 'star'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: "20dp"
                    spacing: "10dp"
                    
                    MDLabel:
                        text: "收藏联系人"
                        theme_text_color: "Primary"
                        font_style: "H6"
                        size_hint_y: None
                        height: self.texture_size[1]
                        
                    MDLabel:
                        text: "您还没有收藏任何联系人"
                        theme_text_color: "Secondary"
                        halign: "center"
                        
            MDBottomNavigationItem:
                name: 'screen3'
                text: '设置'
                icon: 'cog'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: "20dp"
                    spacing: "10dp"
                    
                    MDLabel:
                        text: "设置"
                        theme_text_color: "Primary"
                        font_style: "H6"
                        size_hint_y: None
                        height: self.texture_size[1]
                        
                    MDRaisedButton:
                        text: "打开设置"
                        size_hint: None, None
                        size: "120dp", "40dp"
                        pos_hint: {"center_x": .5}
                        on_press: root.manager.current = 'settings'
''')