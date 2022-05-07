from django.db import models

# Create your models here.
class Major(models.Model):
  name = models.CharField(max_length=255, unique=True)
  slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)

  class Meta:
    ordering: ['-pk']

  def __str__(self):
    #return f'[{self.pk}] {self.name}'
    return str(self.name)
  
  def get_absolute_url(self):
    return f'/{self.slug}/'

class Subject(models.Model):
  major = models.ForeignKey("Major", on_delete=models.CASCADE, null=False, related_name="subject")
  #related_name: ORM 모델을 위한 설정; major.subject.all() 을 한다고 가정할 때 중간 이름을 호출하는 것
  #이때 major.subject 라는 것이 Subject 모델에 생기는 것이 아니라 참조하고 있는 Major 모델에 생성됨
  #on_delte=models.SET_NULL을 할 경우 포린키로 연결되어 있던 Major가 삭제되어도 해당 Subject 필드만 null이 되도록 해줌
  subject_name = models.CharField(max_length=255)
  prof_name = models.CharField(max_length=255)
  memo = models.TextField()
  
  class Meta:
    ordering: ['pk']

  def __str__(self):
    return f'[{self.pk}] | {self.major.name} | {self.subject_name}'
