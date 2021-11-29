from pylatexenc.latex2text import LatexNodes2Text


def convert(tex):
    txt = LatexNodes2Text().latex_to_text(tex)
    return txt
