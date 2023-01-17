from plyer import notification
title = 'Its Time To Take Rest'
message = 'Rest is important for mental Health!   Relax For Few Hours'
notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=10,
                    toast=False)