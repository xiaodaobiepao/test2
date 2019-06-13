from django.db import models

# Create your models here.
#ceshi

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date=models.DateTimeField()
    bread=models.IntegerField(default=0)
    bcommet=models.IntegerField(null=False)
    isDelete=models.BooleanField(default=False)
    class Meta:
        db_table='bookinfo'

    @classmethod
    def create(cls,btitle,bpub_date):
        b=BookInfo
        b.btitle=btitle
        b.bpub_date=bpub_date
        b.bread=0
        b.bcommet=0
        b.isDelete=False
        return b

class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField(default=True)
    hcontent=models.CharField(max_length=1000)
    isDelete=models.BooleanField(default=False)
    book=models.ForeignKey(BookInfo)