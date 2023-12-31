from django import forms
from catalog.models import Product, Version

STOP_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


def check_words(data):
    for word in STOP_WORDS:
        if word in data:
            raise forms.ValidationError(f'Недопустимое слово: {word}')


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data['product_name']
        check_words(name)
        description = cleaned_data['description']
        check_words(description)
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean_is_active(self):
        is_active = self.cleaned_data['is_active']
        product = self.cleaned_data['product']
        if is_active:
            Version.objects.filter(product=product).exclude(id=self.instance.id).update(is_active=False)
        return is_active