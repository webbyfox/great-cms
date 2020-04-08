from django.urls import path

from exportplan import views, recommended_countries, ajax

app_name = 'exportplan'

urlpatterns = [
    path('start/', views.ExportPlanStartView.as_view(), name='start'),
    path('create/', views.ExportPlanCreateView.as_view(), name='create'),
    path('section/target-markets/', views.ExportPlanTargetMarketsView.as_view(), name='target-markets'),
    path('section/<slug:slug>/', views.ExportPlanSectionView.as_view(), name='section'),
    path('ajax/recommended-countries/', recommended_countries.ExportPlanRecommendedCountriesDataView.as_view(), name='ajax-recommended-countries-data'),
    path('ajax/country-data/', ajax.ExportPlanCountryDataView.as_view(), name='ajax-country-data')
]
