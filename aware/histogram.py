# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:10:11 2016

@author: scholl
__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150606-1800"
__status__ = "beta"
__license__ = "GPL"
"""
__author__ = "Marcos V. Scholl"
__email__ = "marcos.vinicius.scholl@gmail.com"
__version__ = "20150606-1800"
__status__ = "beta"
__license__ = "GPL"

"""
Series of data are loaded from a .csv file, and their names are
displayed in a checkable list view. The user can select the series
it wants from the list and plot them on a matplotlib canvas.

Use the sample .csv file that comes with the script for an example
of data series.

Eli Bendersky (eliben@gmail.com)
License: this code is in the public domain
Last modified: 18.05.2009
"""
import sys, os, csv
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure

from datetime import datetime
import datetime as dt

class Histogram(QMainWindow):
    def __init__(self, parent=None):
        super(Histogram, self).__init__(parent)
        self.setWindowTitle('ESSA: Data plotting')
        self.filename = None

        self.data = DataHolder()
        self.series_list_model = QStandardItemModel()

        self.number_group = QButtonGroup() # Number group
        self.time_op1_rb = QRadioButton("5m")
        self.number_group.addButton(self.time_op1_rb)
        self.time_op1_rb.setChecked(True)
        
        self.time_op2_rb = QRadioButton("10m")
        self.number_group.addButton(self.time_op2_rb)
        
        self.time_op3_rb = QRadioButton("30m")
        self.number_group.addButton(self.time_op3_rb)
        
        
        self.time_op4_rb = QRadioButton("1hr")
        self.number_group.addButton(self.time_op4_rb)
        
        self.time_selectet = 0
        self.timeOld = 0
        
        self.create_menu()
        self.create_main_frame()
        self.create_status_bar()
        
        self.update_ui()
        
        #self.on_show()

    def load_file(self, filename=None):
        filename = QFileDialog.getOpenFileName(self,
            'Open a data file', 'Essa_LOG.csv', 'CSV files (*.csv);;All Files (*.*)')
        self.filename = filename
        if filename:
            self.data.load_from_file(filename)
            self.fill_series_list(self.data.series_names())
            self.status_text.setText("Loaded " + filename)
            self.update_ui()
    
    def update_ui(self):
        if self.data.series_count() > 0 and self.data.series_len() > 0:
            self.from_spin.setValue(0)
            self.to_spin.setValue(self.data.series_len() - 1)
            self.to_spin.setMaximum(5000)
            
            for w in [self.from_spin, self.to_spin]:
                w.setRange(0, self.data.series_len() - 1)
                w.setEnabled(True)
        else:
            for w in [self.from_spin, self.to_spin]:
                w.setEnabled(False)
    
    def on_show(self):
        self.axes.clear()        
        self.axes.grid(True)
        
        self.timeOld = self.time_selectet
        if self.number_group.checkedButton().text() == "5m": self.time_selectet = 5
        elif self.number_group.checkedButton().text() == "10m": self.time_selectet = 10
        elif self.number_group.checkedButton().text() == "30m": self.time_selectet = 30
        elif self.number_group.checkedButton().text() == "1hr": self.time_selectet = 60
        #self.time_selectet = self.number_group.checkedButton().text()

        self.data = DataHolder(time_selected=self.time_selectet)
        self.data.time_selectet = self.time_selectet
        #self.data.load_from_file(self.filename)
        has_series = False
        self.data.load_from_file(self.filename)
        

        if self.timeOld != self.time_selectet:
            self.to_spin.setValue(self.data.datalen-1)
        
        #self.update_ui()
        for row in range(self.series_list_model.rowCount()):
            model_index = self.series_list_model.index(row, 0)
            checked = self.series_list_model.data(model_index,
                Qt.CheckStateRole) == QVariant(Qt.Checked)
            name = str(self.series_list_model.data(model_index).toString())
            
            if checked:
                has_series = True
                
                x_from = self.from_spin.value()
                x_to = self.to_spin.value()
                series = self.data.get_series_data(name)[x_from:x_to + 1]
                self.axes.plot(range(len(series)), series, 'o-', label=name)
        
        if has_series and self.legend_cb.isChecked():
            self.axes.legend()
        self.canvas.draw()

    def on_about(self):
        msg = __doc__
        QMessageBox.about(self, "About the plotting", msg.strip())

    def fill_series_list(self, names):
        self.series_list_model.clear()
        
        for name in names:
            item = QStandardItem(name)
            #item.setCheckState(Qt.Unchecked)
            item.setCheckState(Qt.Checked)
            item.setCheckable(True)
            
            self.series_list_model.appendRow(item)
    
    def create_main_frame(self):
        self.main_frame = QWidget()
        
        #plot_frame = QWidget()
        
        self.dpi = 80
        self.fig = Figure((12.5, 3.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        
        self.axes = self.fig.add_subplot(111)
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
        
        log_label = QLabel("Data series:")
        self.series_list_view = QListView()
        self.series_list_view.setModel(self.series_list_model)
        self.series_list_view.setMaximumWidth(200)
        #self.series_list_view.setMinimumWidth(self.series_list_view.sizeHintForColumn(0))
        #list.setFixedSize(list.sizeHintForColumn(0) + 2 * list.frameWidth(), list.sizeHintForRow(0) * list.count() + 2 * list.frameWidth())

        spin_label1 = QLabel('Samples')
        self.from_spin = QSpinBox()
        spin_label2 = QLabel('to')
        self.to_spin = QSpinBox()
        
        layout = QHBoxLayout()  # layout for the central widget
        widget = QWidget(self)  # central widget
        widget.setLayout(layout)
        
        
        
        
        
        spins_hbox = QHBoxLayout()
        spins_hbox.addWidget(spin_label1)
        spins_hbox.addWidget(self.from_spin)
        spins_hbox.addWidget(spin_label2)
        spins_hbox.addWidget(self.to_spin)
        spins_hbox.addStretch(1)
        
        spins_hbox2 = QHBoxLayout()
        spins_hbox2.addWidget(self.time_op1_rb)
        spins_hbox2.addWidget(self.time_op2_rb)
        spins_hbox2.addWidget(self.time_op3_rb)
        spins_hbox2.addWidget(self.time_op4_rb)
        
        self.legend_cb = QCheckBox("Show L&egend")
        self.legend_cb.setChecked(True)
        
        
        self.show_button = QPushButton("&Show")
        self.connect(self.show_button, SIGNAL('clicked()'), self.on_show)
        self.show_button.setMaximumWidth(200)
        left_vbox = QVBoxLayout()
        left_vbox.addWidget(self.canvas)
        left_vbox.addWidget(self.mpl_toolbar)

        right_vbox = QVBoxLayout()
        right_vbox.addWidget(log_label)
        right_vbox.addWidget(self.series_list_view)
        right_vbox.addLayout(spins_hbox)
        right_vbox.addLayout(spins_hbox2)
        right_vbox.addWidget(self.legend_cb)
        
        
        right_vbox.addWidget(self.show_button)
        right_vbox.addStretch(1)
        
        hbox = QHBoxLayout()
        
        hbox.addLayout(right_vbox)
        hbox.addLayout(left_vbox)
        self.main_frame.setLayout(hbox)

        self.setCentralWidget(self.main_frame)
    
    def create_status_bar(self):
        self.status_text = QLabel("Please load a data file")
        self.statusBar().addWidget(self.status_text, 1)

    def create_menu(self):        
        self.file_menu = self.menuBar().addMenu("&File")
        
        load_action = self.create_action("&Load file",
            shortcut="Ctrl+L", slot=self.load_file, tip="Load a file")
        quit_action = self.create_action("&Quit", slot=self.close, 
            shortcut="Ctrl+Q", tip="Close the application")
        
        self.add_actions(self.file_menu, 
            (load_action, None, quit_action))
            
        self.help_menu = self.menuBar().addMenu("&Help")
        about_action = self.create_action("&About", 
            shortcut='F1', slot=self.on_about, 
            tip='About the demo')
        
        self.add_actions(self.help_menu, (about_action,))

    def add_actions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def create_action(  self, text, slot=None, shortcut=None, 
                        icon=None, tip=None, checkable=False, 
                        signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action

class Log(object):
    def __init__(self,name, values,time_update,plus_time):
        self.tag=name
        self.values = []
        self.values.append(values)
        self.plus_time = plus_time
        self.time_update = time_update
        self.now_time = self.time_update + dt.timedelta(minutes=self.plus_time)

    def show(self):
        print self.tag
        print self.values
        
    def __repr__(self):
        return self.tag + ": " + str(self.values)
    
    def add(self, val, time_update):
        self.values.append(val)
        self.time_update = time_update
        self.now_time = self.time_update + dt.timedelta(minutes=self.plus_time)
        
class DataHolder(object):
    """ Just a thin wrapper over a dictionary that holds integer 
        data series. Each series has a name and a list of numbers 
        as its data. The length of all series is assumed to be
        the same.
        
        The series can be read from a CSV file, where each line
        is a separate series. In each series, the first item in 
        the line is the name, and the rest are data numbers.
    """
    def __init__(self, filename=None, time_selected=5):
        self.load_from_file(filename)
        self.logs=[]
        self.tags = []
        self.datalen = 0
        self.time_selectet = time_selected
        
    def ReadCSVasList(self, filename, plus_time):
        try:
            with open(filename):
                reader = csv.reader(open(filename), delimiter=",")
                
                for row in reader:             
                    tim =  row[2].strip()
                    time_complet = datetime.strptime(tim, '%d-%m-%y %H:%M')
                   
                    
                    if row[0] not in  self.tags:
                        self.tags.append(row[0])
                        self.logs.append(Log(row[0], row[1], time_complet, plus_time))
                        #print "logs.append(Log({}, {}, {}, {}))".format(row[0], row[1], time_complet, plus_time)
      
                    elif row[0] in  self.tags:   
                        tim =  row[2].strip()
                        tim = datetime.strptime(tim, '%d-%m-%y %H:%M')
                        
                        #print "\n Tag: ", row[0]
                        for log in self.logs:
                            if log.tag == row[0]:             
                                if tim >= log.now_time:
                                    log.add(row[1],tim)          
            
            
                          
        except IndexError: pass                
        except IOError as (errno, strerror):
                print("I/O error({0}): {1}".format(errno, strerror))    
        return



    def load_from_file(self, filename=None):
        self.data = {}
        self.names = []
        
        
        if filename:
            self.ReadCSVasList(filename, self.time_selectet)
            for tag in self.tags:
                self.names.append(tag)
                
            for log in self.logs:
                self.data[log.tag] = map(float, log.values)
                if self.datalen == 0:
                    self.datalen = len(log.values)
                elif len(log.values) > self.datalen:
                    self.datalen = len(log.values)
    
    def series_names(self):
        """ Names of the data series
        """
        #print "self.names\n",self.names
        return self.names
    
    def series_len(self):
        """ Length of a data series
        """
        #print "self.datalen\n",self.datalen
        return self.datalen
    
    def series_count(self):
        #print "len(self.data)=",len(self.data)
        return len(self.data)

    def get_series_data(self, name):
        #print "self.data[name]\n", self.data[name]
        return self.data[name]


if __name__ == '__main__':
    import sys
  
    app = QApplication(sys.argv)
    mainWin = Histogram()
    mainWin.show()
    sys.exit(app.exec_())

    
"""
def main():
    app = QApplication(sys.argv)
    form = Histogram()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
    
    #~ dh = DataHolder('qt_mpl_data.csv')
    #~ print dh.data
    #~ print dh.get_series_data('1991 Sales')
    #~ print dh.series_names()
    #~ print dh.series_count()
"""   
    
    
    
     