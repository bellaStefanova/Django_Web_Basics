from django import forms

from .models import EmployeeModel

class DepartmentForm(forms.Form):
    department_name = forms.CharField(label="Department Name", max_length=100, required=True)
    department_type = forms.ChoiceField(label="Department Type",
                                        choices=[(1, 'Managers'), (2, 'Team Leads'), (3, 'Employees')],
                                        required=True)
    department_type_radio = forms.IntegerField(widget=forms.RadioSelect(choices=[(1, 'Managers'), (2, 'Team Leads'), (3, 'Employees')]))
    department_with_changed_widget = forms.CharField(label="Department Name with widget with attributes",
                                                    max_length=100, required=True,
                                                    widget=forms.TextInput(attrs={'placeholder': 'Department Name',}))
    
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'
