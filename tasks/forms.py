from django import forms

from tasks.models import *


class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new tasks...'}))

	class Meta:
		model = Task
		fields = '__all__'