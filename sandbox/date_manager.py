from datetime import datetime as dt


class DateManager:

    @property
    def current(self):
        return dt.now()

    @property
    def datetime(self):
        return dt.strftime(self.current, "%Y-%m-%d %H:%M:%S")

    @property
    def date(self):
        return dt.strftime(self.current, "%Y%m%d")

    @property
    def time(self):
        return dt.strftime(self.current, "%H%M%S")

    def format_datetime(self, d_sep: str = '-', t_sep: str = ':'):
        return dt.strftime(self.current, f"%Y{d_sep}%m{d_sep}%d %H{t_sep}%M{t_sep}%S")

    def format_date(self, sep: str = '-'):
        return dt.strftime(self.current, f"%Y{sep}%m{sep}%d")

    def format_time(self, sep: str = ':'):
        return dt.strftime(self.current, f"%H{sep}%M{sep}%S")
