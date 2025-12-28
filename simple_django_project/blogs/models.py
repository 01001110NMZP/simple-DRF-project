from django.db import models

"""
    because you said "just receives messages (including ...)" and didnt specify
    anything else, I decided to make it a blogging web page, so apologies if I did
    something you didnt want me to (aka did something wrong)
"""

class Blog(models.Model):
    """
    A blog model that makes "title", "body_text"
    and "date_added" fields for each blog
    """

    # I had no idea what exactly did you mean by "وضعیت" so I came up with this
    STATUS = [
        ("SENT", "Sent"),
        ("NOT_SENT", "Not Sent"),
        ("DELETED", "Deleted")
    ]

    """
    null = False because I want to make sure this field is filled by the user
    
    CharField, because I want the field to be limited, too long
    titles can mess up the looks of the website 
    
    default = "" because the database needs a default value after some point
    """
    title = models.CharField(null=False,
                             default="",
                             max_length=80)

    # "choices" is just great for these categorical data, got nothing else to say
    status = models.CharField(null=False,
                              choices=STATUS,
                              default=STATUS[1])

    """
    TextField, because the length of a blog shouldn't be limited 
    (unless some guy puts 10^^2 characters in, in that case we 
    should see how generous can we AND the database get)
    """
    body_text = models.TextField(null=False,
                                 default="")

    # just saves the exact time the blog was created, no need to over-explain it
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


