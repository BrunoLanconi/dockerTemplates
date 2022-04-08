from django.db import models


class Sample(models.Model):  # model name
    """
    A model for sample table
    """
    name = models.CharField(max_length=48,  # field max length
                            blank=False,  # required
                            primary_key=False,  # not is a primary key
                            help_text="This represents the sample name presentation.",  # field guide
                            verbose_name="Sample name",  # human readable field definition
                            )  # field definition

    def __str__(self):
        return self.name
