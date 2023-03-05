from django.db import models

# class Post(models.Model):
#     text = models.TextField(
#         verbose_name="Текст поста", help_text="Напишите текст поста"
#     )
#     pub_date = models.DateTimeField(
#         verbose_name="Дата публикации", auto_now_add=True, db_index=True
#     )
#     title = models.ForeignKey(
#         "Group",
#         verbose_name="Заголовок",
#         help_text="Нажмите, чтобы выбрать заголовок",
#         blank=True,
#         null=True,
#         on_delete=models.SET_NULL,
#         related_name="posts",
#     )