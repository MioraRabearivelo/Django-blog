from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.

User = get_user_model()

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre") #unique=True car on ne veut pas avoir 2 article qui a le même titre et verbose_name qui serait affiché à plusieurs endroit
    slug = models.SlugField(max_length=250, unique=True, blank=True) # c'est la version du titre qui serait utilisé dans les urls pour accedé a nos articles
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
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
            cette fonction sauvegarde notre  article dans la base de données, pour modifier automatiquement le slug
            si l' utilisateur n'en specifie pas un
        """
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    @property
    def author_or_default(self):
        return self.author.username if self.author else "L'auteur inconnu"

    def get_absolute_url(self):
        """"
            cette fonction nous redirige vers la page d' accueille après avoir
            valider le contenu du formulaire
        """
        return reverse('posts:home')