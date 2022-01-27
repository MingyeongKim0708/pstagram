from django.urls import path
from django.views.generic.detail import DetailView

from .views import * #views의 모든 함수 임포트
from .models import Photo

app_name = "photo"

urlpatterns = [
    path('', photo_list, name = 'photo_list'), #실행했을 때 root 위치에서 photo_list를 보여줌
    path('detail/<int:pk>/', DetailView.as_view(model = Photo, template_name = 'photo/detail.html'), name = 'photo_detail'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'), #상세한 것은 views에서 이미 적었으므로 여기는 ()를 비워도 된다
    path('update/<int:pk>', PhotoUpdateView.as_view(), name='photo_update'),
    path('delete/<int:pk>', PhotoDeleteView.as_view(), name='photo_delete'),
]