from rest_framework.routers import DefaultRouter

from api.views import (
    PeopleInZoneView, CompanyView, TotalReportView, TotalReportsView, ClientCountReportView, ClientCountReportsView,
    CashReportView, ServicePointsReportView, BitrixReportView, FinanceReportView
)

router = DefaultRouter()
router.register(r'bitrix-reports', BitrixReportView, basename='bitrix_reports')
router.register(r'cash-report', CashReportView, basename='cash_report')
router.register(r'client-count-report', ClientCountReportView, basename='client_count_report')
router.register(r'client-count-reports', ClientCountReportsView, basename='client_count_reports')
router.register(r'companies', CompanyView, basename='companies')
router.register(r'finance-reports', FinanceReportView, basename='finance_reports')
router.register(r'people-in-zone', PeopleInZoneView, basename='people_in_zone')
router.register(r'service-points-report', ServicePointsReportView, basename='service_points_report')
router.register(r'total-report', TotalReportView, basename='total_report')
router.register(r'total-reports', TotalReportsView, basename='total_reports')
urlpatterns = router.urls
