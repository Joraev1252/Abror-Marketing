from django import forms
from abror_marketing.models import BusinessSmmModel, TargetingModel, LogoRoleModel, OurProjectsModel, ContactModel, CarouselModel, CategoriesModels, ServicesModel, MainLogoModel


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


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = CategoriesModels
        fields = ['title1_en', 'title1_ru', 'title1_uz',
                  'title2_en', 'title2_ru', 'title2_uz',
                  'title3_en', 'title3_ru', 'title3_uz',
                  'title4_en', 'title4_ru', 'title4_uz',
                  ]


class ServicesForm(forms.ModelForm):
    class Meta:
        model = ServicesModel
        fields = ['service1_en', 'service1_ru', 'service1_uz',
                  'service2_en', 'service2_ru', 'service2_uz',
                  'service3_en', 'service3_ru', 'service3_uz',
                  'service4_en', 'service4_ru', 'service4_uz',
                  'service5_en', 'service5_ru', 'service5_uz',
                  'service6_en', 'service6_ru', 'service6_uz',
                  'service7_en', 'service7_ru', 'service7_uz',
                  ]


class LogoForm(forms.ModelForm):
    class Meta:
        model = MainLogoModel
        fields = ['image_en', 'image_ru', 'image_uz']




