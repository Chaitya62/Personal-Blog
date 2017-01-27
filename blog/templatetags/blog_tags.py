from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown


register = template.Library()


@register.filter("as_div")

def as_div(form):
	form_as_div = form.as_ul().replace("<ul", "<div").replace("</ul", "</div")
	form_as_div = form_as_div.replace("<li", "<div class='form-group'").replace("</li", "</div")
	return mark_safe(form_as_div)

@register.filter("add_lead")

def add_lead(text):
	new_text = text.replace("<p","<p class='lead'")
	return mark_safe(new_text)

@register.filter(name='markdown')

def markdown_format(text):
	return mark_safe(markdown.markdown(text))


@register.simple_tag

def total_posts():
	return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')

def show_latest_posts(count=5):
	latest_posts = Post.published.order_by('-publish')[:count]
	return {'latest_posts': latest_posts}

@register.assignment_tag

def get_most_commented_posts(count=5):
	return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

