from ui.user_dashboard import UserDashboard


class UI:
    def __init__(self, root):
        self.root = root
        self.current_view = None

    def start(self):
        self._show_user_dashboard()

    def _hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()

        self.current_view = None

    def _show_user_dashboard(self):
        self._hide_current_view()
        self.current_view = UserDashboard(self.root)
