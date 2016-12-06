from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

import re

readmore_showscript = ''.join([
"this.parentNode.style.display='none';",
"this.parentNode.parentNode.getElementsByClassName('more')[0].style.display='inline';",
"return false;",
]);

@register.filter
def readmore(txt, showwords=15):
    global readmore_showscript
    words = re.split(r' ', escape(txt))
    
    if len(words) <= showwords:
        return txt

    # wrap the more part
    words.insert(showwords, '<span class="more" style="display:none;">')
    words.append('</span>')

    # insert the readmore part
    words.insert(showwords, '<span class="readmore">... <a href="#" onclick="')
    words.insert(showwords+1, readmore_showscript)
    words.insert(showwords+2, '">read more</a>')
    words.insert(showwords+3, '</span>')
    words.insert(showwords+4, 'BINGO')

    # Wrap with <p>
    words.insert(0, '<p>')
    words.append('</p>')

    return mark_safe(' '.join(words))


@register.tag
def active(parser, token):
    args = token.split_contents()
    template_tag = args[0]
    if len(args) < 2:
        raise template.TemplateSyntaxError, "%r tag requires at least one argument" % template_tag
    return NavSelectedNode(args[1:])

class NavSelectedNode(template.Node):
    def __init__(self, patterns):
        self.patterns = patterns
    def render(self, context):
        path = context['request'].path
        for p in self.patterns:
            pValue = template.Variable(p).resolve(context)
            if path == pValue:
                return "active" # change this if needed for other bootstrap version (compatible with 3.2)
        return ""

