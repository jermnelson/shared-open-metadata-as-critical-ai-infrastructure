import pathlib
import markdown

from js import console

from puepy import Application, Component, Page, t
from puepy.core import html
from puepy.router import Router

app = Application()
app.install_router(Router, link_mode=Router.LINK_MODE_HASH)

topics = [
   {"name": "AI Agents", "stub": "ai-agents", "icon": "bi-robot"},
   {"name": "LLMs Hallucinations", "stub": "llms-hallucinations", "icon": "bi-chat-square-dots"},
   {"name": "Extinction through AI", "stub": "extinction-ai", "icon": "bi-emoji-dizzy-fill"},
   {"name": "People as AI's Eyelash Mites", "stub": "people-as-ai-eyelash-mite", "icon": "bi-bug-fill"},
   {"name": "People as AI's Mitochondria", "stub": "people-as-ai-mitochondria", "icon": "bi-battery-charging"},
   {"name": "Retrieval Augmented Generation (RAG)", "stub": "rag", "icon": "bi-search"},
   {"name": "Knowledge Graph RAG", "stub": "graph-rag", "icon": "bi-node-plus"},
   {"name": "GLAM Knowledge Graphs", "stub": "glam-graphs", "icon":"bi-book"},
   {"name": "Open Metadata", "stub": "open-metadata", "icon": "bi-patch-check"},
   {"name": "Historical Token Affirmation", "stub": "token-affirmation", "icon": "bi-bookmark-check-fill"},
   {"name": "Introduction to Blue Core", "stub": "intro-blue-core"},
   {"name": "Graph Services", "stub": "blue-core-graph-services"},
   {"name": "Graph RAG", "stub": "blue-core-graph-rag"},
   {"name": "AI Agents", "stub": "blue-core-ai-agents", "icon": "bi-robot-fill"},
   {"name": "MCP Server", "stub": "blue-core-mcp-server"},
   {"name": "Final Thoughts", "stub": "final-thoughts"},
   {"name": "References", "stub": "references"}

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
            with t.div(classes=["col", "mx-auto"]):
                t.h1("Shared Open Metadata as Critical AI Infrastructure", style="text: center")
                t.h2("Jeremy Nelson")
                with t.h3():
                    t.a("jpnelson@stanford.edu", href="mailto:jpnelson@stanford.edu")
            with t.div(class_name="col-2"):
                with t.a(href="https://library.stanford.edu/"):
                    t.img(src="static/img/sul-logo.png", style="width: 300px;", alt="Stanford University Libraries")
        t.hr()


@t.component()
class PresentationFooter(Component):

    def populate(self):
        t.hr()
        with t.footer():
            with t.div(class_name="row"):
                with t.div(class_name="col"):
                    with t.a(href="https://library.stanford.edu/"):
                        t.img(src="static/img/sul-logo.png", alt="Stanford University Libraries", style="width: 300px; padding: 1em;")
                with t.div(class_name="col"):
                    with t.a(href="https://www.dublincore.org/conferences/2025/"):
                        t.img(src="static/img/dcmi-2025-home-banner.svg", style="width: 200px; padding: 1em;", alt="DCMI 2025 Logo")
                    with t.ul(class_name=""):
                         with t.li(class_name=""):
                             t.a("Source Code", href="https://github.com/jermnelson/shared-open-metadata-as-critical-ai-infrastructure")
                with t.div(class_name="col"):
                    with t.a(href="https://bluecore.info/"):
                        t.img(src="static/img/blue-core-v1.png", alt="Blue Core Website", style="width: 300px;")
                    with t.ul(class_name=""):
                         with t.li(class_name=""):
                             t.a("Blue Core Website", href="https://bluecore.info/")
                         with t.li(class_name=""):
                             t.a("Development Blue Core", href="https://dev.bcld.info")
                         with t.li(class_name=""):
                             t.a("Blue Core AI Agents", href="https://github.com/blue-core-lod/bluecore-agents")
                   
            with t.div(class_name="row"):
                with t.div(class_name="col-10"):
                    t.p("Copyright 2025 by Jeremy Nelson, all content licensed under CC0 with source code under Apache2")

@t.component()
class PresentationNavigation(Component):

    def icon(self, topic):
        if "icon" in topic:
            t.i(classes=["bi", topic["icon"]])
        else:
            return ""

    def topic_link(self, topic):
        with t.li(class_name="nav-item"):
            with t.a(classes=["nav-link"], 
                     href=f"#topics/{topic['stub']}"):
                self.icon(topic)
                t.span(f" {topic['name']}")

    def topic_list(self, topics: list):
        for topic in topics:
            self.topic_link(topic)

    
    def populate(self):
        with t.ul(classes=["nav", "flex-column"]):
            with t.li(class_name="nav-item"):
                with t.a(class_name="nav-link", href="/"):
                    self.icon({"icon": "bi-house-door-fill"})
                    t.span(" Home")
            t.li("AI Orientation & Issues", class_name="nav-item")
            self.topic_list(topics[0:3])
            t.li("Cautious Optimism re: People & AI", class_name="nav-item")
            self.topic_list(topics[3:5])
            t.li("RAG Medium Dive")
            self.topic_list(topics[5:7])
            t.li("GLAM Response", class_name="nav-item")
            for topic in topics[7:10]:
                self.topic_link(topic)
            t.li("Blue Core", class_name="nav-item")
            for topic in topics[10:14]:
                self.topic_link(topic)
            t.li("Wrap-up", class_name="nav-item")
            self.topic_link(topics[-1])
            
       


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
