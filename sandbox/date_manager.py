from datetime import datetime as dt


class DateManager:

    @property
    def current(self):
        """Get current date and time by datetime type."""
        return dt.now()

    @property
    def datetime(self):
        """Get current date and time by '%Y-%m-%d %H:%M:%S' format str."""
        return dt.strftime(self.current, "%Y-%m-%d %H:%M:%S")

    @property
    def date(self):
        """Get current date by '%Y%m%d' format str."""
        return dt.strftime(self.current, "%Y%m%d")

    @property
    def time(self):
        """Get current time by '%H%M%S' format str."""
        return dt.strftime(self.current, "%H%M%S")

    def format_datetime(self, d_sep: str = '-', t_sep: str = ':'):
        """
        Current year, month, and date as a string converted to the input d_sep(date separator) format.
        Current hour, minute, and second as a string converted to the input t_sep(time separator) format.
        And return the converted strings as one.

        -----
        :param d_sep: date separator by str type, default is '-'.
        :param t_sep: time separator by str type, default is ':'.

        -----
        :return: f"%Y{d_sep}%m{d_sep}%d %H{t_sep}%M{t_sep}%S".
        """
        return dt.strftime(self.current, f"%Y{d_sep}%m{d_sep}%d %H{t_sep}%M{t_sep}%S")

    def format_date(self, sep: str = '-'):
        """
        Current year, month, and date as a string converted to the input sep(separator) format.

        -----
        :param sep: separator, default is '-'.

        -----
        :return: f"%Y{sep}%m{sep}%d"
        """
        return dt.strftime(self.current, f"%Y{sep}%m{sep}%d")

    def format_time(self, sep: str = ':'):
        """
        Current hour, minute, and second as a string converted to the input sep(separator) format.

        -----
        :param sep: separator, default is ':'.

        -----
        :return: f"%H{sep}%M{sep}%S"
        """
        return dt.strftime(self.current, f"%H{sep}%M{sep}%S")
