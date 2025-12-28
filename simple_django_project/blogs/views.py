from rest_framework import generics
from .models import Blog
from .serializer import BlogSerializer


"""
    Used AI for this file's codes code because I didnt know to do it,
    BUT I also tried to learn it as well and so I'll explain 
    what each line does and explain why I used certain things
    
    Hope this way of learning to not violate any of your rules 
    

    I could've used "generics.ListCreateAPIView" to have both
    GET and POST endpoint in one view, but for more modularity
    I decided to separate them
"""

from django.views.generic import TemplateView

# used Generic Class Based Views (GCBV) because they're easier to work with
class Home(TemplateView):
    template_name = "blogs/home.html" 


# the GET endpoint you mentioned in you PDF and kept the name so the other dev
# working on the project can identify what they're dealing with anywhere in project
class BlogListAPIView(generics.ListAPIView):
    """A read-only endpoint view as a GET endpoint"""

    # so the view receives all the objects made by
    queryset = Blog.objects.all()

    # the serializer that will be using
    serializer_class = BlogSerializer

# POST endpoint
class BlogCreateAPIView(generics.CreateAPIView):
    """A write-only endpoint view as a POST endpoint"""

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

