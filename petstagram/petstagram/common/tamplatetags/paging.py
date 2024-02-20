from django import template

register = template.Library()
@register.inclusion_tag('common/tags/prev_button.html', name='prev_button')
def prev_button():
    return {
        'page_query': '',
        'search_query': '',
        'className': '',


    }