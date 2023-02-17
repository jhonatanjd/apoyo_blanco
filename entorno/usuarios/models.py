from django.db import models

 class soporte(models.Model):
    correo = models.CharField(max_length=50)
    comentario = models.CharField(max_length=500)        

    class Meta:
        db_table ='soporte'
