import io
import sys

from PyQt5 import uic
from PyQt5.QtCore import QMimeData, Qt
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QListWidget

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1280</width>
    <height>720</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>1280</width>
    <height>720</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1280</width>
    <height>720</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="horizontalWidget" native="true">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>1280</width>
      <height>669</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QWidget" name="verticalWidget_3" native="true">
       <layout class="QVBoxLayout" name="verticalLayout_3">
        <item>
         <widget class="QLabel" name="label">
          <property name="font">
           <font>
            <pointsize>16</pointsize>
           </font>
          </property>
          <property name="text">
           <string>TODO</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QListWidget" name="listWidget"/>
        </item>
       </layout>
      </widget>
     </item>
     <item>
      <widget class="QWidget" name="verticalWidget_2" native="true">
       <layout class="QVBoxLayout" name="verticalLayout_2">
        <item>
         <widget class="QLabel" name="label_2">
          <property name="font">
           <font>
            <pointsize>16</pointsize>
           </font>
          </property>
          <property name="text">
           <string>IN PROGRESS</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QListWidget" name="listWidget_2"/>
        </item>
       </layout>
      </widget>
     </item>
     <item>
      <widget class="QWidget" name="verticalWidget" native="true">
       <layout class="QVBoxLayout" name="verticalLayout">
        <item>
         <widget class="QLabel" name="label_3">
          <property name="font">
           <font>
            <pointsize>16</pointsize>
           </font>
          </property>
          <property name="text">
           <string>COMPLETE</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QListWidget" name="listWidget_3"/>
        </item>
       </layout>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1280</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>"""


class Kanban(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.listWidget.addItem("Элемент 1")
        self.listWidget_2.addItem("Элемент 2")

        # Устанавливаем обработчики событий для перетаскивания
        self.listWidget.setAcceptDrops(True)
        self.listWidget_2.setAcceptDrops(True)
        self.listWidget.setDragEnabled(True)
        self.listWidget_2.setDragEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    kan = Kanban()
    kan.show()
    sys.exit(app.exec_())
