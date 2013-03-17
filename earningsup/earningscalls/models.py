from django.db import models

class EarningsCall(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    ticker = models.CharField(max_length=10, blank=True, default='$')
    quarter = models.SmallIntegerField()
    calldate = models.DateField(auto_now=False, auto_now_add=False)
    calltime = models.TimeField(auto_now=False, auto_now_add=False)
    url      = models.URLField(max_length=300)    
    owner = models.ForeignKey('auth.User', related_name='earningscalls')
    
    def save(self, *args, **kwargs):
        super(EarningsCall, self).save(*args, **kwargs)
        
    class Meta:
        ordering = ('created',)
