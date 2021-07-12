from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.db import models

phone_regex = RegexValidator(regex='^0[0-9]{2,}[0-9]{7,}$', message='phone number invalid')


class Entry(models.Model):
    """
    An entry in the phonebook
    """
    username = models.ForeignKey('auth.User', verbose_name=_('صاحب دفترچه'), on_delete=models.PROTECT, null=True,
                                 blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('زمان ساخت'))
    first_name = models.CharField(max_length=100, verbose_name=_('نام'))
    last_name = models.CharField(max_length=100, verbose_name=_('نام خانوادگی'))
    phone_number = models.CharField(validators=[phone_regex], max_length=11, unique=True, verbose_name=_('شماره تلفن'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('دفترچه تلفن')
        verbose_name_plural = _('دفترچه تلفن ها')
