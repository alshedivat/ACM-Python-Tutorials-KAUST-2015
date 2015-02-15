def ensure_dir(d):
    import os, errno
    try:
        os.makedirs(d)
    #except OSError as exc:
    except Exception as exc:
        if exc.errno == errno.EEXIST:
            pass
        else: raise

ensure_dir('mydir')
