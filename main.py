import pathlib
import markdown

from js import console

from puepy import Application, Component, Page, t
from puepy.core import html
from puepy.router import Router

app = Application()
app.install_router(Router, link_mode=Router.LINK_MODE_HASH)

topics = [
   {"name": "AI Agents", "stub": "ai-agents"},
   {"name": "LLMs Hallucinations", "stub": "llms-hallucinations"},
   {"name": "Extinction through AI", "stub": "extinction-ai"},
   {"name": "People as AI's Eyelash Mites", "stub": "people-as-ai-eyelash-mite"},
   {"name": "People as AI's Mitochondria", "stub": "people-as-ai-mitochondria"},
   {"name": "Retrieval Augmented Generation (RAG)", "stub": "rag"},
   {"name": "Knowledge Graph RAG", "stub": "graph-rag"},
   {"name": "GLAM Knowledge Graphs", "stub": "glam-graphs"},
   {"name": "Open Metadata", "stub": "open-metadata"},
   {"name": "Historical Token Affirmation", "stub": "token-affirmation"},
   {"name": "Introduction to Blue Core", "stub": "intro-blue-core"},
   {"name": "Graph Services", "stub": "blue-core-graph-services"},
   {"name": "Graph RAG", "stub": "blue-core-graph-rag"},
   {"name": "AI Agents", "stub": "blue-core-ai-agents"},
   {"name": "MCP Server", "stub": "blue-core-mcp-server"},
    
   {"name": "Final Thoughts", "stub": "final-thoughts"}
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
            with t.div(class_name="col-2"):
                with t.a(href="https://library.stanford.edu/"):
                     t.img(src="static/img/sul-logo.png", style="width: 95%", alt="Stanford University Libraries")
        t.hr()


@t.component()
class PresentationFooter(Component):

    def populate(self):
        t.hr()
        with t.footer():
            with t.div(class_name="row"):
                with t.div(class_name="col-10"):
                    t.p("Copyright 2025 by Jeremy Nelson, all content licensed under CC0 with source code under Apache2")
                with t.div(class_name="col-2"):
                    t.img(src="static/img/qr-code.png", alt="Presentation QR code", style="width: 50px;")


@t.component()
class PresentationNavigation(Component):

    def icon(self, topic):
        if "icon" in topic:
            t.i(classes=["bi", topic["icon"]])

    def topic_link(self, topic):
        with t.li(class_name="nav-item"):
            t.a(topic["name"], 
                classes=["nav-link"], 
                href=f"#topics/{topic['stub']}") 
    
    def populate(self):
        with t.ul(classes=["nav", "flex-column"]):
            with t.li(class_name="nav-item"):
                with t.a(class_name="nav-link", href="/"):
                    self.icon("Home", {"icon": "bi-house-door-fill"})
            t.li("AI Orientation & Issues", class_name="nav-item")
            for topic in topics[0:2]:
                self.topic_link(topic)
            t.li("Cautious Optimism re: People & AI", class_name="nav-item")
            for topic in topics[2:5]:
                self.topic_link(topic)
            t.li("RAG Medium Dive")
            t.li("GLAM Response", class_name="nav-item")
            for topic in topics[5:7]:
                self.topic_link(topic)
            t.li("Blue Core", class_name="nav-item")
            for topic in topics[7:12]:
                self.topic_link(topic)
            t.li("Wrap-up", class_name="nav-item")
            for topic in topics[12:]:
                self.topic_link(topic)
       


@app.page("/topics/<topic_stub>")
class TopicPage(Page):
    props = ["topic_stub"]

    def populate(self):
        md_path = docs / f"{self.topic_stub}.md"
        t.presentation_head()
        with t.div(class_name="row"):
            with t.div(class_name="col-3"):
                t.presentation_navigation()
            with t.div(classes=["col", "overflow-scroll"]):
                raw_html = markdown.markdown(md_path.read_text(), extensions=['extra']) 
                t(html(raw_html))
        t.presentation_footer()


@app.page()
class DCMIPresentationPage(Page):

    def populate(self):
        welcome_path = docs / "welcome.md"
        t.presentation_head()
        with t.div(class_name="row"):
            with t.div(class_name="col-3"):
                t.presentation_navigation()
            with t.div(classes=["col", "overflow-scroll"]):
                raw_html = markdown.markdown(welcome_path.read_text(), extensions=['extra'])
                console.log(raw_html)
                t(html(raw_html))
        t.presentation_footer()


app.mount("#app")
