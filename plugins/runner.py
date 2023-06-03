from docutils.parsers.rst import Directive
from docutils.nodes import raw
import urllib.parse

class RunnerDirective(Directive):
    has_content = True

    def run(self):
        code = "\n".join(self.content)
        encoded_code = urllib.parse.quote(code)
        html = f"""
        <iframe src="/_static/runner/runner.html?initCode={encoded_code}" height="800" width="800" title="Runner"></iframe>
        """
        return [raw("", html, format="html")]
        
def setup(app):
    app.add_directive("runner", RunnerDirective)