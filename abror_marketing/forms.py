from django import forms
from abror_marketing.models import BusinessSmmModel, TargetingModel, LogoRoleModel, OurProjectsModel, ContactModel, CarouselModel


class BusinessSmmForm(forms.ModelForm):
    class Meta:
        model = BusinessSmmModel
        fields = ['title_en', 'title_ru', 'title_uz', 'body1_en', 'body1_ru', 'body1_uz', 'body2_en', 'body2_ru', 'body2_uz', 'image_en', 'image_ru', 'image_uz']


class TargetForm(forms.ModelForm):
    class Meta:
        model = TargetingModel
        fields = ['title_en', 'title_ru', 'title_uz', 'body1_en', 'body1_ru', 'body1_uz', 'body2_en', 'body2_ru', 'body2_uz', 'image_en', 'image_ru', 'image_uz']


class LogoForm(forms.ModelForm):
    class Meta:
        model = LogoRoleModel
        fields = ['title_en', 'title_ru', 'title_uz', 'body1_en', 'body1_ru', 'body1_uz', 'body2_en', 'body2_ru', 'body2_uz', 'image_en', 'image_ru', 'image_uz']


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = OurProjectsModel
        fields = ['title_en', 'title_ru', 'title_uz', 'body1_en', 'body1_ru', 'body1_uz', 'body2_en', 'body2_ru', 'body2_uz', 'image1_en', 'image1_ru', 'image1_uz', 'image2_en', 'image2_ru', 'image2_uz']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['nickname', 'number']


class CarouselForm(forms.ModelForm):
    class Meta:
        model = CarouselModel
        fields = ['image']



