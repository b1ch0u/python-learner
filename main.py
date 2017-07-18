import sys, traceback
import json

from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.properties import ListProperty, StringProperty

import LabelB

TESTS_FILENAME = 'tests.json'

RED = (1, 0.2, 0.2, 1)
GREEN = (0.2, 1, 0.2, 1)
BLUE = (0.2, 0.2, 1, 1)

def parse_tests_metadata(tests_filename):
    with open(tests_filename, 'r') as f:
        res = json.load(f)
    for test in res:
        with open(test['filename'], 'r') as f:
            test['test_code'] = f.read()
    return res

class CodeTester(ScrollView):
    spinner_text = StringProperty()
    spinner_values = ListProperty()
    instructions_text = StringProperty()
    result_color = ListProperty()
    result_text = StringProperty()

    def __init__(self, tests_filename):
        super(CodeTester, self).__init__()
        self.result_color = BLUE
        self.tests = parse_tests_metadata(tests_filename)
        self.current_test = self.tests[0]
        self.spinner_values = [t['name'] for t in self.tests]
        self.spinner_text = self.current_test['name']

    def change_test(self):
        # TODO ugly ! change self.tests to a dict
        self.spinner_text = self.ids.tests_spinner.text
        self.current_test = next(v for v in self.tests if v['name'] == self.spinner_text)
        self.spinner_text = self.current_test['name']
        self.instructions_text  = self.current_test['description']
        self.result_color = BLUE
        self.result_text = ''

    def test_code(self):
        text = self.ids.code_input.text
        try:
            ns = {}
            exec(text, ns)
            exec(self.current_test['test_code'], ns)
            res = str(ns['res'])
        except:
            res = traceback.format_exc()
        self.result_text = res
        self.result_color = GREEN if res == 'OK' else RED

class SimpleKivy(App):
    def build(self):
        return CodeTester(TESTS_FILENAME)

if __name__ == '__main__':
    SimpleKivy().run()
