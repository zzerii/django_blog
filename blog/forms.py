from django import forms
from .models import Post,Comment

# Validator 함수 정의
# title 입력 필드의 길이 체크 < 3 : 3보다 작으면 error
def min_length_3_validator(value):
    if len(value)<3:
        raise forms.ValidationError('title은 3글자 이상 다시 입력해주세요!')


class PostForm(forms.Form):
    title=forms.CharField(validators=[min_length_3_validator])
    #title=forms.CharField()
    text=forms.CharField(widget=forms.Textarea)



# ModelForm을 상속 받는 postModelForm 클래스 선언
class PostModelForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','text',)


# ModelForm을 상속 받는 CommentModelForm 클래스 선언
class CommentModelForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('author', 'text',)