# -*- coding: utf-8 -*-
"""
Simple data acquisition from serial port.

QuDi is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

QuDi is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with QuDi. If not, see <http://www.gnu.org/licenses/>.

Copyright (C) 2016 Jan M. Binder jan.binder@uni-ulm.de
"""

from core.base import Base
from pyqtgraph.Qt import QtCore
from core.util.mutex import Mutex
from collections import OrderedDict
from interface.simple_data_interface import SimpleDataInterface
import numpy as np
import time

import visa


class SimpleAcq(Base, SimpleDataInterface):
    """
    """
    _modclass = 'simple'
    _modtype = 'hardware'

    # connectors
    _out = {'simple': 'Simple'}

    def __init__(self, manager, name, config, **kwargs):
        c_dict = {'onactivate': self.activation, 'ondeactivate': self.deactivation}
        Base.__init__(self, manager, name, configuration=config, callbacks = c_dict)

    def activation(self, e):
        self.rm = visa.ResourceManager('@py')
        print(self.rm.list_resources())
        self.my_instrument = self.rm.open_resource('ASRL/dev/ttyUSB0::INSTR', baud_rate=115200)


    def deactivation(self, e):
        self.my_instrument.close()
        self.rm.close()


    def getData(self):
        try:
            return int(self.my_instrument.read_raw().decode('utf-8').rstrip())
        except:
            return 0

    def getChannels(self):
        return 1