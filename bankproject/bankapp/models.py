from django.db import models


class DistrictModel(models.Model):
    Did=models.IntegerField(primary_key=True)
    Dname = models.CharField(max_length=100)

    class Meta:
        db_table = "districttable"


class BranchModel(models.Model):
    Bid = models.IntegerField(primary_key=True)
    Bname = models.CharField(max_length=100)
    Did=models.IntegerField()


    class Meta:
        db_table = "branchtable"


