from django import forms


class FormBase(forms.Form):
    def to_payload(self, post_query_dict):
        payload = {}

        for key in self.data.keys():
            if key in post_query_dict:
                payload[key] = self.data.get(key)

        return payload
