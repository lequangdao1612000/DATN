# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'layout_info_tableui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sqlite3


class Ui_Info_Table(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.db = 'Database\huyquang.db'
        # self.db_to_df()
        # self.show_table()
    
    def db_to_df(self):
        self.conn = sqlite3.connect(self.db)
        self.df = pd.read_sql_query("SELECT * FROM parking", self.conn)
    
    def show_table(self):
        df = self.df.drop(['id', "img_path"], axis=1)
        self.table.setRowCount(len(df))
        self.table.setColumnCount(len(df.columns))
        self.table.setHorizontalHeaderLabels(df.columns)
        header = self.table.horizontalHeader()
        self.table.verticalHeader().setVisible(False)
        for i in range(df.columns.size):
            # header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)       
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        for i in range(len(df)):
            for j in range(len(df.columns)):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(df.iloc[i, j])))
    
    def open_image(self, item):
        row = item.row()
        data = self.df.iloc[row]
        img_path = data[-1]
        print(img_path)
    
    def setupUi(self):
        self.setObjectName("Table Info")
        self.resize(711, 441)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet("background: beige")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.query = QtWidgets.QTextEdit(self.groupBox)
        self.query.setGeometry(QtCore.QRect(10, 40, 281, 31))
        self.query.setText("Search...")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.query.sizePolicy().hasHeightForWidth())
        self.query.setSizePolicy(sizePolicy)
        self.query.setStyleSheet("background: white")
        self.query.setObjectName("query")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.table = QtWidgets.QTableWidget(self)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.gridLayout.addWidget(self.table, 0, 1, 2, 1)
        self.qlabel_frame = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_frame.sizePolicy().hasHeightForWidth())
        self.qlabel_frame.setSizePolicy(sizePolicy)
        self.qlabel_frame.setMinimumSize(QtCore.QSize(300, 300))
        self.qlabel_frame.setStyleSheet("background: black")
        self.qlabel_frame.setObjectName("qlabel_frame")
        self.gridLayout.addWidget(self.qlabel_frame, 1, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Info Table", "Info Table"))

    def slot_query(self, s):
        # self.table.setCurrentItem(None)
        if not s:
            print("No query")
            return
        items = self.table.findItems(
            s, QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive)
        rows = [item.row() for item in items]
        for i in range(self.table.rowCount()):
            self.table.setRowHidden(i, not i in rows) 
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Info_Table()
    ui.db = r"C:\Users\ASUS\Desktop\daoquang1612\parking_project\datn\Database\huyquang.db"
    ui.db_to_df()
    ui.show_table()
    ui.show()
    sys.exit(app.exec_())