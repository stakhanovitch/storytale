from django import forms
from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit,Field
from crispy_forms.bootstrap import FormActions

class MySignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MySignupForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            FormActions(
                Submit('submit', 'Sign-up', css_class = 'btn-primary')
                ),
        )
        #self.helper = helper
        """
        #Special stuff from allauth to be rewrited in the crispy way
        {% if redirect_field_value %}
        <input type="hidden" name="{{ redirect_field_name }}" value="{{ redirect_field_value }}" />
        {% endif %}
        """
