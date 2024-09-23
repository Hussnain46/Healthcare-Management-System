from django import forms
from user.models import Doctor
from .models import Appointment, TimeSlot, AvailableDay



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'appointment_date', 'appointment_time']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if user and hasattr(user, 'patient'):
            self.fields['doctor'].queryset = Doctor.objects.all()




class AvailabilityForm(forms.Form):
    available_days = forms.MultipleChoiceField(
        choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
                 ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'),
                 ('Sunday', 'Sunday')],
        widget=forms.CheckboxSelectMultiple,
        label="Select Days"
    )
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))







class TimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['time']  # Add other fields if needed




class UpdateAvailabilityForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['time']  # Just showing time for update

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].widget.attrs.update({'class': 'form-control'})




class AppointmentForm(forms.Form):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), required=True)
    day = forms.ModelChoiceField(queryset=AvailableDay.objects.all())
    time = forms.ModelChoiceField(queryset=TimeSlot.objects.all())


