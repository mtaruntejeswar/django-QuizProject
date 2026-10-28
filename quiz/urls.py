from django.urls import path
from . import views

urlpatterns = [
    path('teacher/dashboard/',views.teachers_dashboard,name='teachers-dashboard'),
    path('teacher/quizzes/create/',views.create_quiz,name='create-quiz'),
    path('teacher/quizzes/<quiz_id>/edit/',views.edit_quiz,name='edit-quiz'),
    path('teacher/quizzes/<quiz_id>/questions/',views.view_quiz_questions,name='view-quiz-questions'),
    path('teacher/quizzes/<int:quiz_id>/questions/add/',views.add_question,name='add-question'),
    path('teacher/questions/<int:question_id>/edit/',views.edit_question,name='edit-question'),
    # path('teacher/questions/<int:question_id>/delete/',views.delete_question,name='delete-question'),
    path('teacher/quizzes/<int:quiz_id>/preview/',views.quiz_preview,name='quiz-preview'),
    # path('teacher/quizzes/<int:quiz_id>/publish/',views.publish_quiz,name='quiz-preview'),
    # path('teacher/quizzes/<int:quiz_id>/delete/',views.publish_quiz,name='quiz-preview'),
    path('teacher/quizzes/<int:quiz_id>/results/',views.quiz_results,name='quiz-results'),

]

# /student/quizzes/
# /student/quizzes/<quiz_id>/
# /student/quizzes/<quiz_id>/attempt/
# /student/attempts/<attempt_id>/submit/
# /student/attempts/<attempt_id>/result/
# /student/attempts/<attempt_id>/review/
# /student/attempt-history/