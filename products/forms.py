from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=3,
        max_length=50,
        label="Ім'я"
    )

    message = forms.CharField(
        min_length=10,
        widget=forms.Textarea,
        label="Повідомлення"
    )

    def clean_message(self):
        message = self.cleaned_data["message"]

        if "bad" in message.lower():
            raise forms.ValidationError(
                "Некоректне повідомлення"
            )

        return message