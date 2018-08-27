#!/usr/bin/env python3
from cortexutils.analyzer import Analyzer


class ActiveDirectoryAnalyzer(Analyzer):
    def __init__(self):
        Analyzer.__init__(self)
        #self.filepath = self.get_param('file', None, 'File parameter is missing.')

    def summary(self, raw):
        taxonomies = []
        

        return {'taxonomies': taxonomies}



    def run(self):
        results = []


        self.report({'results': results})


if __name__ == '__main__':
    ActiveDirectoryAnalyzer().run()
