from django.core.exceptions import ValidationError


def validate_img_png(img):
    if not img.name.endswith('.png'):
        raise ValidationError('Image must be a PNG file')
    return img
