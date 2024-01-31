from django import forms

class DepartmentForm(forms.Form):
    department_name = forms.CharField(label="Department Name", max_length=100, required=True)
    department_type = forms.ChoiceField(label="Department Type",
                                        choices=[(1, 'Managers'), (2, 'Team Leads'), (3, 'Employees')],
                                        required=True)
    department_type_radio = forms.IntegerField(widget=forms.RadioSelect(choices=[(1, 'Managers'), (2, 'Team Leads'), (3, 'Employees')]))