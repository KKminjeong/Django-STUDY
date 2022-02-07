from django.shortcuts import render, redirect
from .forms import SimpleUploadForm, ImageUploadForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .cv_functions import cv_detect_face



# Create your views here.
def first_view(request):
    return render(request, 'opencv_webapp/first_view.html', {})


def simple_upload(request):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.FILES)
        # 비어있는 Form에 사용자가 업로드한 데이터를 넣고 검증합니다.
        form = SimpleUploadForm(request.POST, request.FILES)

        if form.is_valid():
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile) # 경로명을 포함한 파일명 & 파일 객체
            uploaded_file_url = fs.url(filename) # 업로드된 이미지 파일의 URL을 얻어내 Template에게 전달

            context = {'form': form, 'uploaded_file_url': uploaded_file_url} # filled form
            return render(request, 'opencv_webapp/simple_upload.html', context)

    else: # request.method == 'GET' (DjangoBasic 실습과 유사한 방식입니다.)
        form = SimpleUploadForm()
        context = {'form': form} # empty form
        return render(request, 'opencv_webapp/simple_upload.html', context)


def detect_face(request):
    if request.method == 'POST':
        # 비어있는 Form에 사용자가 업로드한 데이터를 넣고 검증합니다.
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Form에 채워진 데이터를 DB에 실제로 저장하기 전에 변경하거나 추가로 다른 데이터를 추가할 수 있음
            # post는 save() 후 DB에 저장된 ImageUploadModel 클래스 객체 자체를 갖고 있게 됨 (record에 해당)
            post = form.save(commit=False)
            post.save() # DB에 실제로 Form 객체('form')에 채워져 있는 데이터를 저장
            # print(form.instance)                # ImageUploadModel object (2)
            # print(form.instance.document)       # images/2020/02/17/ses.jpg
            # print(form.instance.document.name)  # images/2020/02/17/ses.jpg
            # print(form.instance.document.url)   # /media/images/2020/02/17/ses.jpg
            imageURL = settings.MEDIA_URL + form.instance.document.name
            cv_detect_face(settings.MEDIA_ROOT_URL + imageURL) # 추후 구현 예정

            return render(request, 'opencv_webapp/detect_face.html', {'form':form, 'post':post})

    else:
         form = ImageUploadForm() # empty form
         return render(request, 'opencv_webapp/detect_face.html', {'form':form})
