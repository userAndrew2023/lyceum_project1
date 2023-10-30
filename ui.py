import io
import sys

from PyQt5 import uic
from PyQt5.QtCore import QMimeData, Qt, QSize
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QListWidget, QPushButton, QVBoxLayout, QWidget, \
    QLabel, QLineEdit, QMessageBox, QAbstractItemView

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
         <widget class="QPushButton" name="addTodo">
          <property name="font">
           <font>
            <pointsize>12</pointsize>
           </font>
          </property>
          <property name="text">
           <string>Add</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLineEdit" name="lineEdit">
          <property name="font">
           <font>
            <pointsize>11</pointsize>
           </font>
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
         <widget class="QPushButton" name="addProgress">
          <property name="font">
           <font>
            <pointsize>12</pointsize>
           </font>
          </property>
          <property name="cursor">
           <cursorShape>PointingHandCursor</cursorShape>
          </property>
          <property name="text">
           <string>Add</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLineEdit" name="lineEdit_2">
          <property name="font">
           <font>
            <pointsize>11</pointsize>
           </font>
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
         <widget class="QPushButton" name="addComplete">
          <property name="font">
           <font>
            <pointsize>12</pointsize>
           </font>
          </property>
          <property name="cursor">
           <cursorShape>PointingHandCursor</cursorShape>
          </property>
          <property name="text">
           <string>Add</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLineEdit" name="lineEdit_3">
          <property name="font">
           <font>
            <pointsize>11</pointsize>
           </font>
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
     <height>21</height>
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

        self.addTodo.clicked.connect(self.addTodoListener)
        self.addProgress.clicked.connect(self.addProgressListener)
        self.addComplete.clicked.connect(self.addCompleteListener)

        self.listWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget.setAcceptDrops(True)
        self.listWidget_2.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget_2.setAcceptDrops(True)

    def addTodoListener(self):
        if len(self.lineEdit.text().strip()) != 0:
            self.listWidget.addItem(self.lineEdit.text().strip())

    def addProgressListener(self):
        if len(self.lineEdit_2.text().strip()) != 0:
            self.listWidget_2.addItem(self.lineEdit_2.text().strip())

    def addCompleteListener(self):
        if len(self.lineEdit_3.text().strip()) != 0:
            self.listWidget_3.addItem(self.lineEdit_3.text().strip())

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        print('d')
        # Получаем элемент и источник
        item = e.source().currentItem()
        source = e.source()

        # Удаляем элемент из источника
        source.takeItem(source.row(item))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    kan = Kanban()
    kan.show()
    sys.exit(app.exec_())
