import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = LeafNode("a", "link", {"href": "https://www.google.com", "target": "_blank"})
        node3 = ParentNode(
            "div",
            [
                LeafNode("p", "I love coding"),
                LeafNode(None, "Boring plain text"),
                LeafNode("p", "HTML is kind of annoying"),
                LeafNode(None, "More boring old text")
            ]
        )
        self.assertEqual("HTMLNode(a, link, None, {'href': 'https://www.google.com', 'target': '_blank'})", repr(node))
        self.assertEqual("LeafNode(a, link, {'href': 'https://www.google.com', 'target': '_blank'})", repr(node2))
        self.assertEqual('ParentNode(div, [LeafNode(p, I love coding, None), LeafNode(None, Boring plain text, None), LeafNode(p, HTML is kind of annoying, None), LeafNode(None, More boring old text, None)], None)', repr(node3))

    def test_to_html(self):
        node = LeafNode("p", "This is a test")
        node2 = LeafNode("a", "link", {"href": "https://www.google.com", "target": "_blank"})
        node3 = ParentNode(
            "div",
            [
                LeafNode("p", "I love coding"),
                LeafNode(None, "Boring plain text"),
                LeafNode("p", "HTML is kind of annoying"),
                LeafNode(None, "More boring old text")
            ],
            {"class": "cool", "id": "biz"}
            )
        self.assertEqual(node.to_html(), "<p>This is a test</p>")
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com" target="_blank">link</a>')
        self.assertEqual(node3.to_html(), '<div class="cool" id="biz"><p>I love coding</p>Boring plain text<p>HTML is kind of annoying</p>More boring old text</div>')

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()
