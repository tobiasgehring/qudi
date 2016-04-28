# -*- coding: utf-8 -*-
"""
Flipmirror preposttask

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

Copyright (C) 2015-2016 Jan M. Binder jan.binder@uni-ulm.de
"""

from logic.generic_task import PrePostTask

class Task(PrePostTask):

    def __init__(self, name, runner, references, config):
        super().__init__(name, runner, references, config)
        print('Task {} added!'.format(self.name))

    def preExecute(self):
        if ('switchlogic' in self.ref
            and 'sequence' in self.config):
                logic = self.ref['switchlogic']
                for element in self.config['sequence']:
                    if element[2]:
                        logic.switches[element[0]][element[1]].switchOn(element[1])
                    else:
                        logic.switches[element[0]][element[1]].switchOff(element[1])
        else:
            self.runner.logMsg('No switching sequence configured for pre/post task {}'.format(self.name), msgType='error')


    def postExecute(self):
        if ('switchlogic' in self.ref
            and 'sequence' in self.config):
                logic = self.ref['switchlogic']
                for element in reversed(self.config['sequence']):
                    if element[2]:
                        logic.switches[element[0]][element[1]].switchOff(element[1])
                    else:
                        logic.switches[element[0]][element[1]].switchOn(element[1])
        else:
            self.runner.logMsg('No switching sequence configured for pre/post task {}'.format(self.name), msgType='error')

