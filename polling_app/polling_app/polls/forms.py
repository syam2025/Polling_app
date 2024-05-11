
from django import forms
from .models import Poll, Choice

class PollForm(forms.ModelForm):
    choice1 = forms.CharField(max_length=100, required=False)
    choice2 = forms.CharField(max_length=100, required=False)
    choice3 = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Poll
        fields = ['question']


class VoteForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']  # Assuming 'choice_text' is the field you want to display in the form

    def __init__(self, poll, *args, **kwargs):
        super(VoteForm, self).__init__(*args, **kwargs)
        self.fields['choice_text'].queryset = poll.choice_set.all()

