from braces.views import JSONResponseMixin, AjaxResponseMixin


class HighChartsBasicView(JSONResponseMixin, AjaxResponseMixin):

    title = None
    subtitle = None

    chart_type = None
    chart_width = None
    chart_height = None

    legend = None

    tooltip = None
    tooltip_point_format = None

    plot_options = {}

    series = []

    def get_data(self):
        data = {}
        # Title is "kinda mandatory"
        data['title'] = {}
        data['title']['text'] = self.title or None

        # Subtitle option
        if self.subtitle:
            data['subtitle'] = {}
            data['subtitle']['text'] = self.subtitle

        # Chart design and style
        data['chart'] = {}
        if self.chart_type:
            data['chart']['type'] = self.chart_type
        if self.chart_width:
            data['chart']['width'] = self.chart_width
        if self.chart_height:
            data['chart']['height'] = self.chart_height

        # Legend
        if self.legend:
            data['legend'] = self.legend

        # tooltip
        if self.tooltip or self.tooltip_point_format:
            if not self.tooltip:
                self.tooltip = {}
            data['tooltip'] = self.tooltip
            if self.tooltip_point_format:
                data['tooltip']['pointFormat'] = self.tooltip_point_format

        # plotOptions is just dict dumping
        if self.plot_options:
            data['plotOptions'] = self.plot_options

        data['series'] = self.get_series()

        return data

    def get(self, request, *args, **kwargs):
        return self.get_ajax(request, *args, **kwargs)

    def get_ajax(self, request, *args, **kwargs):
        return self.render_json_response(self.get_data())

    def get_series(self):
        """
        Define your own series.
        """
        return self.series


class HighChartsDualAxisView(HighChartsBasicView):

    x_axis = {}
    x_axis_categories = []

    y_axis = [] # Multiple yAxis is possible.

    def get_data(self):
        data = super(HighChartsDualAxisView, self).get_data()
        data['xAxis'] = self.get_x_axis()
        data['xAxis']['categories'] = self.get_x_axis_categories()
        y_axis = self.get_y_axis()
        if y_axis:
            # LineChart does not display with empty yAxis.
            data['yAxis'] = y_axis
        return data

    def get_x_axis(self):
        """
        Define your own xAxis.
        """
        return self.x_axis

    def get_x_axis_categories(self):
        """
        Define your own xAxis categories.
        """
        return self.x_axis_categories

    def get_y_axis(self):
        """
        Define your own yAxis.
        """
        return self.y_axis
