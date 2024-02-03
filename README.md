# mdit-py-toc <!-- omit in toc -->

A table of contents (TOC) plugin for [markdown-it-py](https://markdown-it-py.readthedocs.io/en/latest/)
based on [markdown-it-toc-done-right](https://github.com/nagaozen/markdown-it-toc-done-right).

- [Installation](#installation)
  - [Install using poetry](#install-using-poetry)
  - [Install using pip](#install-using-pip)
- [Options](#options)
- [Usage](#usage)

## Installation

### Install using poetry

Because **mdit-py-toc** is a plugin you most likely need a tool to
handle Python package dependencies and Python environments. Therefore we
strongly recommend using [poetry].

You can install the latest stable release and add it as a dependency for your
current project using [poetry]

```
poetry add mdit-py-toc
```

### Install using pip

> [!NOTE]
> The `pip install` command does no longer work out-of-the-box in newer
> distributions like Ubuntu >= 23.04 because of [PEP 668](https://peps.python.org/pep-0668).

You can install the latest stable release from the Python Package Index (pypi)
using [pip]

```
python -m pip install mdit-py-toc
```

## Options

| Name      | Description                                                            | Default               |
| --------- | ---------------------------------------------------------------------- | --------------------- |
| pattern   | The pattern serving as the TOC placeholder in your markdown            | `r"^(\[TOC\]")`       |
| level     | Minimum level to apply anchors on or iterable of selected levels       | `(1, 2)`              |
| list_type | Type of list (`"ul"` for unordered, `"ol"` for ordered)                | `"ul"`                |
| slug_func | Function to convert heading title text to id slugs for link references | `mdit_py_toc.slugify` |

## Usage

```python
from markdown_it import MarkdownIt
from mdit_py_toc import toc_plugin

md = MarkdownIt().use(toc_plugin, list_type="ol")
markdown = """
# A Page

[TOC]

## Section 1

## Section 1
"""
html = md.render(markdown)
```

[poetry]: https://python-poetry.org/
[pip]: https://pip.pypa.io/
