def statusCode_200(driver_instance):
    status = driver_instance.current_url
    code = status[19:]
    value = "200"
    if value == (code):
        return True
    else:
        return False

def statusCode_305(driver_instance):
    status = driver_instance.current_url
    code = status[19:]
    value = "305"
    if value == (code):
        return True
    else:
        return False

def statusCode_404(driver_instance):
    status = driver_instance.current_url
    code = status[19:]
    value = "404"
    if value == (code):
        return True
    else:
        return False

def statusCode_500(driver_instance):
    status = driver_instance.current_url
    code = status[19:]
    value = "500"
    if value == (code):
        return True
    else:
        return False