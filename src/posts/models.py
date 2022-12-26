from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.

User = get_user_model()
class BlogPost(models.Model):

    """
        We use this class to initialise and save a post created and edit by an user
    """

    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    # SET_NULL because if an user is removed in database, his post is not removed from the database
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)

    # created_on is blank=True and not auto now, cause the user can choose to not published his post the moment when he create and edit a post
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")
    thumbnail = models.ImageField(blank=True, upload_to='blog')

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
            This function save our article in the database, and edit automatically the
            slug if the user didn't specify one
        """
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    @property
    def author_or_default(self):
        """
            this function return the user name for an post, and make autamatically
        """
        return self.author.username if self.author else "L'auteur inconnu"

    def get_absolute_url(self):
        """
            redirect to the home page after having validate the form
        """
        return reverse('posts:home')