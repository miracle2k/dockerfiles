### gitolite on docker

Runs an SSH server, serving gitolite as the git@ user.

On first start, can run "gitolite setup" with a starting ssh key you provided.

On subsequent starts, will run "gitolite setup" everytime to integrate any
outside changes.

### Examples

New installation:

    docker run -e SSH_KEY="$(cat ~/.ssh/id_rsa.pub)" elsdoerfer/gitolite

Use an existing gitolite installation:

    docker run -v /var/vcroot/git:/home/git/repositories elsdoerfer/gitolite

### Environment variables:

**SSH_KEY**

SSH public key for initial access to the gitolite-admin repository. If you
have an existing gitolite-admin repository, you may skip this.

**GIT_CONFIG_KEYS**
**LOCAL_CODE** (example value: *$ENV{HOME}/local*)

These will be inserted into gitolite.rc.

### Directories you could bind mount

/home/git/repositories
  The actual git repositories will be stored here.


## Further customization

If you need to use things like custom hooks, you have different options:

* Point the *LOCAL_CODE* variable to something like "$ENV{HOME}/.gitolite/local", use the gitolite-admin repo to provide the data.
* You could bind mount files into the container (xxx: how to provide certain files (gitolite.rc) before setup runs?)
* Derive a custom Docker image, ADD the files (xxx: how to provide certain files (gitolite.rc) before setup runs?)
* Manually interact with a container, but lose it disposible nature.