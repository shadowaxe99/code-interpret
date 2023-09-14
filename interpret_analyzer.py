import pylint.lint
from radon import complexity, metrics


class FileAnalyzer:
    def __init__(self):
        pass

    def syntax_analyzer(self, file):
        pylint_output = pylint.lint.Run([file], do_exit=False)
        return pylint_output.linter.msg_status

    def logic_analyzer(self, file):
        radon_output = complexity.cc_visit(file)
        return radon_output

    def performance_analyzer(self, file):
        with open(file, 'r') as f:
            file_content = f.read()
        radon_mi_output = metrics.mi_visit(file_content, True)
        return radon_mi_output