from modeltranslation.translator import register, TranslationOptions
from abror_marketing.models import BusinessSmmModel, TargetingModel, LogoRoleModel, OurProjectsModel, CategoriesModels, ServicesModel, MainLogoModel


@register(BusinessSmmModel)
class BusinessTranslationOptions(TranslationOptions):
    fields = ['title', 'body1', 'body2', 'image']


@register(TargetingModel)
class TargetTranslationOptions(TranslationOptions):
    fields = ['title', 'body1', 'body2', 'image']


@register(LogoRoleModel)
class LogoTranslationOptions(TranslationOptions):
    fields = ['title', 'body1', 'body2', 'image']


@register(OurProjectsModel)
class ProjectsTranslationOptions(TranslationOptions):
    fields = ['title', 'body1', 'body2', 'image1', 'image2']


@register(CategoriesModels)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ['title1', 'title2', 'title3', 'title4']


@register(ServicesModel)
class ServicesTranslationOptions(TranslationOptions):
    fields = ['service1', 'service2', 'service3', 'service4', 'service5', 'service6', 'service7']


@register(MainLogoModel)
class LogoTranslationOptions(TranslationOptions):
    fields = ['image']