from django.db import models


class seller(models.Model):
    s_name=models.CharField(max_length=100,default="")
    s_contact=models.IntegerField(default=0)
    s_id=models.IntegerField(default=0)
    s_address=models.CharField(max_length=120,default="")
    s_email=models.CharField(max_length=110,default="")

    s_pass = models.CharField(max_length=110,null=False)

    def __str__(self):
        return self.s_name


class buyer(models.Model):
    b_name = models.CharField(max_length=100, default="")
    b_contact = models.CharField(max_length=128, default='')
    b_id = models.IntegerField(default=0)
    b_address = models.CharField(max_length=120, default="")
    b_email = models.EmailField(max_length=110, default="")
    b_pass = models.CharField(max_length=110,null=False)

    def __str__(self):
        return self.b_name


class payment(models.Model):
    payment_id=models.IntegerField(default=0)
    payment_ammount=models.IntegerField(default=0)
    payment_date=models.IntegerField(default=0)

    def __str__(self):
        return self.payment_id


class car(models.Model):
     car_name = models.CharField(max_length=100, default="")
     car_id=models.IntegerField(default=0)
     price_per_day=models.IntegerField(default=0)
     car_type = models.CharField(max_length=100, default="")
     car_img = models.CharField(max_length=100, default="")

     def __str__(self):
         return self.car_name


class sold(models.Model):
    s_id = models.ForeignKey(seller,default=0,on_delete=models.CASCADE)
    b_id = models.ForeignKey(buyer,default=0,on_delete=models.CASCADE)
    f_id = models.ForeignKey(car,default=0,on_delete=models.CASCADE)
    payment_id = models.ForeignKey(payment,default=0,on_delete=models.CASCADE)

    def __str__(self):
        return self.payment_id

