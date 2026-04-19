from rest_framework.throttling import ScopedRateThrottle, SimpleRateThrottle


class PostCreateThrottle(ScopedRateThrottle):
    scope = 'post_create'


class LoginThrottle(ScopedRateThrottle):
    scope = 'login'


class IPRateThrottle(SimpleRateThrottle):
    scope = 'ip'

    def get_cache_key(self, request, view):
        return self.get_ident(request)