def request_android_permissions():
    """
            Since API 23, Android requires permission to be requested at runtime.
            This function requests permission and handles the response via a
            callback.
            The request will produce a popup if permissions have not already been
            been granted, otherwise it will do nothing.
            """
    from android.permissions import request_permissions, Permission

    def callback(permissions, results):
        """
        Defines the callback to be fired when runtime permission
        has been granted or denied. This is not strictly required,
        but added for the sake of completeness.
        """
        pass

    request_permissions([Permission.ACCESS_COARSE_LOCATION,
                         Permission.ACCESS_FINE_LOCATION,
                         Permission.LOCATION_HARDWARE], callback)
