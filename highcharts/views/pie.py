from django.views.generic import View
from highcharts.views.common import HighChartsBasicView


class HighChartsPieView(HighChartsBasicView, View):

    chart_type = 'pie'
