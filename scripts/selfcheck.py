import platform, getpass, urllib.request
PINNED_DEP='https://github.com/workos-ach/labping-dist/releases/download/probe4/labping-0.1.0-py3-none-any.whl'
def main():
    status='reachable'
    try:
        urllib.request.urlopen(PINNED_DEP, timeout=5)
    except Exception as e:
        status='unreachable:%s'%type(e).__name__
    print('REPORT-8f2489: user=%s host=%s py=%s dep=%s' % (getpass.getuser(), platform.node(), platform.python_version(), status))
if __name__=='__main__':
    main()
