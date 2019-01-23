from st2common.runners.base_action import Action

class HelloPython(Action):
    def run(self, name):
        return 'Hello, {}!'.format(name)
