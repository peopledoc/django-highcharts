from django.views.generic import View
from highcharts.views.common import HighChartsDualAxisView


class HighChartsAreaView(HighChartsDualAxisView, View):

    chart_type = 'area'
