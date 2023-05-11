import js
from pyodide.ffi import to_js

TEMPLATE = """
<div class="reveal">
  <div class="slides">
    <section data-markdown>
      <textarea data-template>
        {content}
      </textarea>
    </section>
  </div>
</div>
"""

def show(filename):
    with open(filename) as f:
        content = f.read()

    slides = TEMPLATE.format(content=content)
    js.document.body.insertAdjacentHTML("beforeend", slides)

    options = js.Object()
    options.plugins = to_js([js.RevealMarkdown])
    js.Reveal.initialize(options)
