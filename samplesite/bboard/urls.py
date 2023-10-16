from django.urls import path, include
from django.views.decorators.cache import cache_page
from rest_framework.routers import DefaultRouter

from bboard.views import (index, BbCreateView, detail, BbByRubricView,
                          BbDetailView, rubrics, bbs, search, BbEditView,
    # APIRubrics, APIRubricDetail,
                          APIRubricViewSet)

router = DefaultRouter()
router.register('rubrics', APIRubricViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('rubrics/', rubrics, name='rubrics'),

    # path('api/v1/rubrics/<int:pk>/', api_rubric_detail),
    # path('api/v1/rubrics/', api_rubrics),

    #
    #
    # path('api/v1/rubrics/', APIRubrics.as_view()),
    # path('api/v1/rubrics/<int:pk>/', APIRubricDetail.as_view()),

    path('api/v1/', include(router.urls)),
    path('bbs/<int:rubric_id>/', bbs, name='bbs'),
    path('page/<int:page>/', index, name='page'),

    path('<int:rubric_id>/', cache_page(60 * 5)(BbByRubricView.as_view()), name='by_rubric'),

    path('<int:rubric_id>/page/<int:page>/', BbByRubricView.as_view(), name='rubric_page'),
    path('read/<int:rec_id>/', detail, name='read'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BbEditView.as_view(), name='update'),

    path('search/', search, name='search'),
]
