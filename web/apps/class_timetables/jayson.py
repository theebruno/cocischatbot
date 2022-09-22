# import fitz
# import json
#
# from .models import ClassTimetable
#
#
# def upload_timetable_logic(request):
#     file_uploaded = ClassTimetable.objects.order_by('timestamp').last()
#     document = fitz.open(file_uploaded)
#     page = document.loadPage(14)  # enter page
#     text = page.getText('dict')
#     # print(text)
#
#     with open('intents_class_timetables.json', 'w+') as f:
#         text_data = json.dump(text, f)
