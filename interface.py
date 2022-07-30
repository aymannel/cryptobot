import sys
import matplotlib
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        fig = Figure(figsize=(16, 8), dpi=100)
        self.ax1 = fig.add_subplot(2, 2, (1, 2))
        self.ax2 = fig.add_subplot(2, 2, (3, 4))
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setFixedWidth(1200)
        self.setFixedHeight(600)
       
        btc = yf.Ticker("BTC")
        aapl = yf.Ticker("AAPL")
        self.plot_ticker(btc, aapl)

    def plot_ticker(self, ticker1, ticker2):
        start = datetime.now() - timedelta(days=120)
        end = datetime.now()
        
        data1 = ticker1.history(start=start, end=end, interval="1d")
        data2 = ticker2.history(start=start, end=end, interval="1d")
        
        price1 = data1['High']
        price2 = data2['High']
        time1 = data1.index
        time2 = data2.index

        qtcanvas = MplCanvas()
        qtcanvas.ax1.plot(time1, price1)
        qtcanvas.ax1.set_xlim(min(time1), max(time1))
        qtcanvas.ax1.set_title('BTC')

        qtcanvas.ax2.plot(time2, price2)
        qtcanvas.ax2.set_xlim(min(time2), max(time2))
        qtcanvas.ax2.set_title('AAPL')
        
        self.setCentralWidget(qtcanvas)
        self.show()



app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
