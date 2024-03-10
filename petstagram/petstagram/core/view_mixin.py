from django.contrib.auth import mixins as auth_mixins


class OwnerRequiredMixin(auth_mixins.LoginRequiredMixin):
    user_field = 'user'
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.user = getattr(obj, self.user_field,None)
        if obj.user != self.request.user:
            raise PermissionError('You are not the owner of this pet')
        return obj