init python in _wm_dashboard_app:
    class Dashboard(object):
        DETAILS = 0
        SUBJECTS = 1
        COMPLETED = 2

        def __init__(self):
            self.display = self.DETAILS
            self.selected_test = None

    class AIEntry(object):
        def __init__(self, thumbnail, wm_id, name, age):
            super(AIEntry, self).__init__()
            self.thumbnail = thumbnail
            self.wm_id = wm_id
            self.name = name
            self.age = age

    monika = AIEntry("monika_thumb", "WM125255140", "Monika", 18)
    sayori = AIEntry("sayori_thumb", "WM138222255", "Sayori", 18)
    natsuki = AIEntry("natsuki_thumb", "WM250153255", "Natsuki", 18)
    yuri = AIEntry("yuri_thumb", "WM194140255", "Yuri", 18)