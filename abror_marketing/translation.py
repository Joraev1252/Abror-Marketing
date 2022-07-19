from modeltranslation.translator import register, TranslationOptions
from abror_marketing.models import BusinessSmmModel, TargetingModel, LogoRoleModel, OurProjectsModel


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

