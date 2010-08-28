from django.db import models
from django.forms import ModelForm, DateInput, PasswordInput
from django.forms.extras.widgets import SelectDateWidget

class Member(models.Model):
    login_id = models.CharField(max_length = 30, unique = True, null = False)
    login_pw = models.CharField(max_length = 30, null = False)
    user_name = models.CharField(max_length = 50, null = False)
    email = models.EmailField(unique = True)
    birthday = models.DateField(null = False)
    
    class Meta:
        db_table = 'member'
        
class MemberForm(ModelForm):
    class Meta:
        model = Member
        widgets = {'birthday':SelectDateWidget(years=range(1900, 2010)), 'login_pw' : PasswordInput}