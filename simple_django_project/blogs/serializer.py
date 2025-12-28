from rest_framework import serializers
from .models import Blog

# used AI for this one, but learned it in the way:

"""
    ModelSerializer, because despite the official docs that uses Serializer
    and configures every field manually, ModeSerializer does it automatically
    
    so a better choice for this one
    
    
    btw serializers are used to convert rows of data in our database
    to be presented as JSON files/formats and vice versa, this way data
    manipulation will be easier because in this way we'll be using
    python to manipulate data rather than SQL commands 
    
"""
class BlogSerializer(serializers.ModelSerializer):

    # inner class meta (which I think comes from "metadata"
    # is the config of the outer class)
    class Meta:
        model = Blog
        fields = "__all__"
