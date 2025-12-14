from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from utils.export_manager import ExportManager


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.export_manager = ExportManager()


# 加载KV文件
Builder.load_string('''
<SettingsScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        MDToolbar:
            title: "设置"
            elevation: 10
            left_action_items: [["arrow-left", lambda x: app.root.current = 'main']]
            
        ScrollView:
            MDGridLayout:
                cols: 1
                padding: "10dp"
                spacing: "5dp"
                
                MDCard:
                    orientation: "vertical"
                    padding: "15dp"
                    size_hint_y: None
                    height: theme_settings_box.height + 30
                    
                    MDBoxLayout:
                        id: theme_settings_box
                        orientation: 'vertical'
                        spacing: "15dp"
                        
                        MDLabel:
                            text: "主题设置"
                            font_style: "H6"
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDBoxLayout:
                            orientation: 'horizontal'
                            spacing: "10dp"
                            
                            MDLabel:
                                text: "浅色主题"
                                size_hint_x: 0.7
                                
                            MDSwitch:
                                id: theme_switch
                                active: False
                                
                            MDLabel:
                                text: "深色主题"
                                size_hint_x: 0.7
                
                MDCard:
                    orientation: "vertical"
                    padding: "15dp"
                    size_hint_y: None
                    height: language_settings_box.height + 30
                    
                    MDBoxLayout:
                        id: language_settings_box
                        orientation: 'vertical'
                        spacing: "15dp"
                        
                        MDLabel:
                            text: "语言设置"
                            font_style: "H6"
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDDropDownItem:
                            id: language_dropdown
                            text: "简体中文"
                            on_release: None  # 打开语言选择菜单
                
                MDCard:
                    orientation: "vertical"
                    padding: "15dp"
                    size_hint_y: None
                    height: export_settings_box.height + 30
                    
                    MDBoxLayout:
                        id: export_settings_box
                        orientation: 'vertical'
                        spacing: "15dp"
                        
                        MDLabel:
                            text: "数据导出"
                            font_style: "H6"
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDRaisedButton:
                            text: "导出为CSV"
                            size_hint: None, None
                            size: "150dp", "40dp"
                            pos_hint: {"center_x": .5}
                            on_press: None  # 导出为CSV
                            
                        MDRaisedButton:
                            text: "导出为JSON"
                            size_hint: None, None
                            size: "150dp", "40dp"
                            pos_hint: {"center_x": .5}
                            on_press: None  # 导出为JSON
                            
                        MDRaisedButton:
                            text: "备份数据"
                            size_hint: None, None
                            size: "150dp", "40dp"
                            pos_hint: {"center_x": .5}
                            on_press: None  # 备份数据
''')