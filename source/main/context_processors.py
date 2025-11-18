def current_user(request):
    """Context processor to provide current_user variable for templates"""
    return {
        'current_user': request.user,
    }

