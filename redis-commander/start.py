#!/usr/bin/env python

import os, re

# No urlparse in base OS image
# http://stackoverflow.com/a/17892757/15677
def url_path_to_dict(path):
    pattern = (r'^'
               r'((?P<schema>.+?)://)?'
               r'(?P<netloc>.*?)'
               r'(:(?P<port>\d+?))?'
               r'(?P<path>/.*?)?'
               r'(?P<query>[?].*?)?'
               r'$'
               )
    regex = re.compile(pattern)
    m = regex.match(path)
    d = m.groupdict() if m is not None else None

    return d

args = []

if 'REDIS_URL' in os.environ:
    url = Exception()  # just an object with __dict__
    url.__dict__ = url_path_to_dict(os.environ['REDIS_URL'])
    if '@' in url.netloc:
        auth, host = url.netloc.split('@', 1)
        if ':' in auth:
            user, pw = auth.split(':', 1)
            args.append(('--redis-password', pw))
        else:
            user = auth
        if user:
            print('Redis URL contains username, ignored')
    else:
        host = url.netloc
    args.append(('--redis-host', host))
    if url.path:
        args.append(('--redis-db', url.path))
    if url.port:
        args.append(('--redis-port', url.port))

other_args = {
    '--port': 'PORT',
    '--http-auth-username': 'HTTP_AUTH_USERNAME',
    '--http-auth-password': 'HTTP_AUTH_PASSWORD'
}
for arg, env in other_args.items():
    if env in os.environ:
        args.append((arg, os.environ[env]))


final = ['redis-commander']
[final.extend(a)  for a in args]
os.execvp('redis-commander', final)
