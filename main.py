import pathlib
import markdown

from puepy import Application, Component, Page, t
from puepy.core import html
from puepy.router import Router

app = Application()
app.install_router(Router, link_mode=Router.LINK_MODE_HASH)

topics = [
   {"name": "Welcome", "stub": "welcome"},
   {"name": "AI Agents", "stub": "ai-agents"},
   {"name": "LLMs Hallucinations", "stub": "llms-hallucinations"},
   {"name": "Retrieval Augmented Generation (RAG)", "stub": "rag"},
   {"name": "Knowledge Graph RAG", "stub": "graph-rag"},
   {"name": "GLAM Knowledge Graphs", "stub": "glam-graphs"},
   {"name": "Open Metadata", "stub": "open-metadata"},
   {"name": "GLAM Historical Token Affirmation", "stub": "glam-token-affirmation"},
   {"name": "Introduction to Blue Core", "stub": "intro-blue-core"},
   {"name": "Blue Core Graph Services", "stub": "blue-core-graph-services"},
   {"name": "Blue Core Graph RAG", "stub": "blue-core-graph-rag"},
   {"name": "Blue Core AI Agents", "stub": "blue-core-ai-agents"},
   {"name": "Blue Core MCP Server", "stub": "blue-core-mcp-server"},
   {"name": "Extinction through AI", "stub": "extinction-ai"}, 
   {"name": "Final Thoughts Or Cautious Optimism", "stub": "final-thoughts-cautious-optimism"}
]

topic_names = {}
for topic in topics:
    topic_names[topic['stub']] = topic['name']

home = pathlib.Path(".").parent
docs = home / "doc"

@t.component()
class PresentationHead(Component):

    def populate(self):
        with t.div(class_name="row"):
            with t.div(class_name="col-2"):
                t.img(src="static/img/dcmi-2025-home-banner.svg", style="width: 90%", alt="DCMI 2025 Logo")
                t.h5("22 October 2025")
            with t.div(class_name="col"):
                t.h1("Shared Open Metadata as Critical AI Infrastructure")
                t.h2("Jeremy Nelson, Stanford University Libraries")
        t.hr()


@t.component()
class PresentationFooter(Component):

    def populate(self):
        t.hr()
        with t.footer():
            t.p("Copyright 2025 by Jeremy Nelson, all content licensed under CC0 with source code under Apache2")


@t.component()
class PresentationNavigation(Component):
    
    def populate(self):
        with t.ul(classes=["nav", "flex-column"]):
            for topic in topics:
                with t.li(class_name="nav-item"):
                    t.a(topic["name"], 
                        classes=["nav-link", "active"], 
                        href=f"#topics/{topic['stub']}")


@app.page("/topics/<topic_stub>")
class TopicPage(Page):
    props = ["topic_stub"]

    def populate(self):
        md_path = docs / f"{self.topic_stub}.md"
        t.presentation_head()
        with t.div(class_name="row"):
            with t.div(class_name="col-3"):
                t.presentation_navigation()
            with t.div(class_name="col"):
                raw_html = markdown.markdown(md_path.read_text(), extensions=['extra'])
                t(html(raw_html))
        t.presentation_footer()


@app.page()
class DCMIPresentationPage(Page):

    def populate(self):
        t.presentation_head()
        with t.div(class_name="row"):
            with t.div(class_name="col-3"):
                t.presentation_navigation()
            with t.div(class_name="col"):
                t.img(src="static/img/qr-code.png", alt="Presentation QR code")
        t.presentation_footer()


app.mount("#app")
