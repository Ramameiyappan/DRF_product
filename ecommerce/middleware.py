class SessionJWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.session.get('access')
        if token:
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {token}'
            print("JWT added to request:", request.META['HTTP_AUTHORIZATION'])
        else:
            print("No JWT in session")
        return self.get_response(request)