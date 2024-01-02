from django import template

register = template.Library()


@register.inclusion_tag('Shared/HeaderSite.html')
def site_header_inclusion():
    return {}




@register.inclusion_tag('Shared/FooterSite.html')
def site_footer_inclusion():
    return {}
