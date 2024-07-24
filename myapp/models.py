from django.db import models

# Create your models here.


class Catalog(models.Model):
    book_name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)

    class Meta:
        db_table = 'catalog'


class Book(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=250)
    books = models.ManyToManyField(Book)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    author_name = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"Comment by {self.author_name} on {self.article}"


class ArticleLike(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    user_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Like by {self.user_name} on {self.article}"


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    user_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Like by {self.user_name} on {self.comment}"
