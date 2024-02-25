import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QUrl, Qt, QTimer, QStringListModel
from PIL import Image
from PyQt5.QtWebEngineWidgets import QWebEngineView
import re
import requests
import time
import psutil
import GPUtil


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BrowsEase")
        self.showMaximized()
        self.default_widgets()
        self.setWindowIcon(QIcon('browser\icon.png'))
        self.show()
        self.suggestions_cache = {}

        
    
    def default_widgets(self):    
        #background
        bg_img = Image.open("browser\\blackscreen.jpg")
        background_img = QPixmap.fromImage(QImage(bg_img.tobytes(), bg_img.width, bg_img.height, bg_img.width * 3, QImage.Format_RGB888))
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(background_img))
        self.setPalette(palette)
        
        # Search bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Enter Search or Enter Web URL")
        self.search_bar.setFont(QFont("Segoe Print", 9))
        self.search_bar.returnPressed.connect(self.search_result)
        self.tab_widget = QTabWidget(self)
        self.add_tab()
        
        self.completer = QCompleter(self)
        self.search_bar.setCompleter(self.completer)
        self.search_bar.textChanged.connect(self.update_search_suggestions)

        # Main layout
        main_layout = QVBoxLayout(self)
        
        self.add_tab_button = QPushButton("Add Tab", self)
        self.add_tab_button.setFont(QFont("Segoe Print", 9))
        self.add_tab_button.clicked.connect(self.add_tab)
        self.add_tab_button.setMinimumWidth(120) 
        
        self.remove_tab_button = QPushButton("Remove Tab", self)
        self.remove_tab_button.setFont(QFont("Segoe Print", 9))
        self.remove_tab_button.clicked.connect(self.rem_tab)
        self.remove_tab_button.setMinimumWidth(120)
        
        self.home_button = QPushButton(self)
        self.home_button.clicked.connect(self.home)
        self.home_icon = QIcon("browser\home.png")
        self.home_button.setIcon(self.home_icon)
        self.home_button.setMinimumWidth(35)
        self.home_button.setMinimumHeight(28)
        
        
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignLeft)
        button_layout.addWidget(self.home_button)
        button_layout.addWidget(self.add_tab_button)
        button_layout.addWidget(self.remove_tab_button)
         
        
        self.ctrl_t_shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_T), self)
        self.ctrl_t_shortcut.activated.connect(self.add_tab)
        
        self.ctrl_w_shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_W), self)
        self.ctrl_w_shortcut.activated.connect(self.rem_tab)

        main_layout.addWidget(self.search_bar)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.tab_widget)     

    def update_search_suggestions(self):
        search_text = self.search_bar.text()
        if search_text in self.suggestions_cache:
            suggestions = self.suggestions_cache[search_text]
        else:
            suggestions = self.fetch_google_suggestions(search_text)
            self.suggestions_cache[search_text] = suggestions

        self.completer.setModel(QStringListModel(suggestions))


    def fetch_google_suggestions(self, query):
        base_url = "http://suggestqueries.google.com/complete/search"
        params = {
            "q": query,
            "client": "chrome",
        }

        response = requests.get(base_url, params=params)
        suggestions = response.json()[1] if response.status_code == 200 else []

        return suggestions       

    def add_tab(self):  
        self.new_tab = QWidget()
        self.tab_widget.addTab(self.new_tab, "New Tab")
        
        image_label = QLabel(self.new_tab)
        pixmap = QPixmap("browser\\background.jpg")  
        image_label.setPixmap(pixmap)
        
        self.gmail_shortcut_button = QPushButton("Gmail", self.new_tab)
        self.gmail_shortcut_button.setFont(QFont("Segoe Print", 14))
        self.gmail_shortcut_button.clicked.connect(self.gmail_shortcut)
        self.gmail_shortcut_button.setGeometry(30, 30, 90, 30)
        self.gmail_shortcut_button.setStyleSheet("background-color: transparent; color: white; border: 3px solid white; border-radius: 5px; text-align: center; font-weight: bold;")
        
        self.photos_shortcut_button = QPushButton("Photos", self.new_tab)
        self.photos_shortcut_button.setFont(QFont("Segoe Print", 14))
        self.photos_shortcut_button.clicked.connect(self.photos_shortcut)
        self.photos_shortcut_button.setGeometry(130,30,90,30)
        self.photos_shortcut_button.setStyleSheet("background-color: transparent; color: white; border: 3px solid white; border-radius: 5px; text-align: center; font-weight: bold;")
        
        self.drive_shortcut_button = QPushButton("Drive", self.new_tab)
        self.drive_shortcut_button.setFont(QFont("Segoe Print", 14))
        self.drive_shortcut_button.clicked.connect(self.drive_shortcut)
        self.drive_shortcut_button.setGeometry(30,80,90,30)
        self.drive_shortcut_button.setStyleSheet("background-color: transparent; color: white; border: 3px solid white; border-radius: 5px; text-align: center; font-weight: bold;")

        self.youtube_shortcut_button = QPushButton("YouTube", self.new_tab)
        self.youtube_shortcut_button.setFont(QFont("Segoe Print", 14))
        self.youtube_shortcut_button.clicked.connect(self.youtube_shortcut)
        self.youtube_shortcut_button.setGeometry(130, 80, 90, 30)
        self.youtube_shortcut_button.setStyleSheet("background-color: transparent; color: white; border: 3px solid white; border-radius: 5px; text-align: center; font-weight: bold;")

        self.gmail_shortcut_button.setObjectName("Gmail")
        self.photos_shortcut_button.setObjectName("Photos")
        self.drive_shortcut_button.setObjectName("Drive")
        self.youtube_shortcut_button.setObjectName("Youtube")

        layout = QVBoxLayout(self.new_tab)
        layout.addWidget(image_label)
        self.tab_widget.setCurrentWidget(self.new_tab) 
        
        
    def rem_tab(self):
        current_index = self.tab_widget.currentIndex()
        if current_index >= 0:
            self.tab_widget.removeTab(current_index)
        else:
            QApplication.quit()

    
    def home(self):
        pass
    
    def gmail_shortcut(self):
       pass

    def photos_shortcut(self):
        pass
    
    def drive_shortcut(self):
        pass
    
    def youtube_shortcut(self):
        pass
    
    def search_result(self):
        self.suggestions_cache.clear()
        search_text = self.search_bar.text() 
        self.handle_search_result(search_text)
        
    def handle_search_result(self, search_text):
        current_tab = self.tab_widget.currentWidget()
       
        for widget in current_tab.findChildren(QWidget):
            if widget.objectName() in ["Gmail", "Photos", "Drive","Youtube"]:
                widget.setParent(None)
        
        for i in reversed(range(current_tab.layout().count())):
            current_tab.layout().itemAt(i).widget().setParent(None)
        
        url_pattern = re.compile(r"^(https?://)?([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,6})([/\w.-]*)*")
        
        if url_pattern.match(search_text):
            if not re.match(r'^https?://', search_text):
                search_text = 'https://' + search_text
                web_view = QWebEngineView(current_tab)
                web_view.setUrl(QUrl(search_text))
                current_tab.layout().addWidget(web_view)
                web_view.urlChanged.connect(self.update_search_bar)
            else:
                web_view = QWebEngineView(current_tab)
                web_view.setUrl(QUrl(search_text))
                current_tab.layout().addWidget(web_view)
                web_view.urlChanged.connect(self.update_search_bar)
        else:
            google_search_url = QUrl("https://www.google.com/search?q=" + search_text)
            web_view = QWebEngineView(current_tab)
            web_view.setUrl(google_search_url)
            current_tab.layout().addWidget(web_view)
            web_view.urlChanged.connect(self.update_search_bar)
    
    def update_search_bar(self, qurl):
        if qurl.isValid():
            self.search_bar.setText(qurl.toString())
            self.search_bar.setCursorPosition(0)
    

            
        

app = QApplication(sys.argv)
mw = MainWindow()
sys.exit(app.exec_())
