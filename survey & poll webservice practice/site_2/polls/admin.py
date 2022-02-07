from django.contrib import admin
from .models import Question, Choice


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1 # Default로 보여줄 Choice 입력 slot의 수


class QuestionAdmin(admin.ModelAdmin):
    # fieldsets 변수명은 고정입니다.
    fieldsets = [
        # ('field 집합의 소제목', {'fields': ['field 이름 1', 'field 이름 2', ...]}),
        ("Question title", {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # list_display 변수명은 고정입니다. (소괄호는 생략되어도 무방)
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date'] # pub_date(설문조사 생성 시간)을 기준으로 필터 기능 추가
    search_fields = ['question_text'] # question_text(설문조사 주제)를 기준으로 검색 기능 추가


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
