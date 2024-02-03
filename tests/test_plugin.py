import unittest

from markdown_it import MarkdownIt

from mdit_py_toc import toc_plugin


class TocPluginTestCase(unittest.TestCase):
    def test_render(self) -> None:
        md = MarkdownIt().use(toc_plugin)
        markdown = """
# A Page

[TOC]

## Section 1

## Section 2
"""
        expected = """<h1>A Page</h1>
<nav>
<ul>
<li><a href="#a-page">A Page</a><ul>
<li><a href="#section-1">Section 1</a></li>
<li><a href="#section-2">Section 2</a></li>
</ul></li>
</ul></nav>
<h2>Section 1</h2>
<h2>Section 2</h2>
"""
        html = md.render(markdown)
        self.assertEqual(html, expected)

    def test_render_ordered_list(self) -> None:
        md = MarkdownIt().use(toc_plugin, list_type="ol")
        markdown = """
# A Page

[TOC]

## Section 1

## Section 2
"""
        expected = """<h1>A Page</h1>
<nav>
<ol>
<li><a href="#a-page">A Page</a><ol>
<li><a href="#section-1">Section 1</a></li>
<li><a href="#section-2">Section 2</a></li>
</ol></li>
</ol></nav>
<h2>Section 1</h2>
<h2>Section 2</h2>
"""
        html = md.render(markdown)
        self.assertEqual(html, expected)

    def test_render_slug_func(self) -> None:
        def test_slugify(text: str) -> str:
            return text.upper().replace(" ", "*")

        md = MarkdownIt().use(toc_plugin, slug_func=test_slugify)
        markdown = """
# A Page

[TOC]

## Section 1

## Section 2
"""
        expected = """<h1>A Page</h1>
<nav>
<ul>
<li><a href="#A*PAGE">A Page</a><ul>
<li><a href="#SECTION*1">Section 1</a></li>
<li><a href="#SECTION*2">Section 2</a></li>
</ul></li>
</ul></nav>
<h2>Section 1</h2>
<h2>Section 2</h2>
"""
        html = md.render(markdown)
        self.assertEqual(html, expected)

    def test_render_pattern(self) -> None:
        md = MarkdownIt().use(toc_plugin, pattern=r"^\*\*TOC\*\*")
        markdown = """
# A Page

**TOC**

## Section 1

## Section 2
"""
        expected = """<h1>A Page</h1>
<nav>
<ul>
<li><a href="#a-page">A Page</a><ul>
<li><a href="#section-1">Section 1</a></li>
<li><a href="#section-2">Section 2</a></li>
</ul></li>
</ul></nav>
<h2>Section 1</h2>
<h2>Section 2</h2>
"""
        html = md.render(markdown)
        self.assertEqual(html, expected)

    def test_render_levels(self) -> None:
        md = MarkdownIt().use(toc_plugin, level=1)
        markdown = """
# A Page

[TOC]

## Section 1

## Section 2
"""
        expected = """<h1>A Page</h1>
<nav>
<ul>
<li><a href="#a-page">A Page</a><ul>
</ul></li>
</ul></nav>
<h2>Section 1</h2>
<h2>Section 2</h2>
"""
        html = md.render(markdown)
        self.assertEqual(html, expected)
