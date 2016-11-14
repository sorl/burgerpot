from django import forms
from .models import Bug
from material import Layout, Row, Fieldset


class BugForm(forms.ModelForm):
    layout = Layout(
        'seen',
        Fieldset('',
            Row('browser_name', 'browser_version', 'browser_name_other'),
            Row('operating_system', 'operating_system_version', 'operating_system_other'),
        ),
        'description',
        Row('severity', 'priority'),
        'steps_to_reproduce',
        'actual_behavior',
        'expected_behavior',
        Row('troubleshooting', 'workaround'),
        'screenshot',
    )

    class Meta:
        model = Bug
        exclude = ['submitter', 'status', 'created', 'updated']
