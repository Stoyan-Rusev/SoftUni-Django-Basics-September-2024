class ReadOnlyMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_readonly_fields()

    def make_readonly_fields(self):
        for field_name, field in self.fields.items():
            field.widget.attrs['disabled'] = True
