from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Photo

# Create your views here.
def photo_list(request):
    photos = Photo.objects.all() #Photo 클래스에 등록되어있는 모든 사진 정보를 가져옴
    return render(request, 'photo/list.html', {'photos':photos})

class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    #원래 CreateView에 있는 메소드를 오버라이딩(리모델링하는 것)
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save() #이상이 없으면 데이터베이스에 저장
            return redirect('/') #메인페이지로 이동
        else:
            return self.render_to_response({'form':form}) #문제가 있으면 그대로 작성 페이지에 표시

class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'

class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/' #잘 삭제하면 main으로 이동
    template_name = 'photo/delete.html'

