### gitolite on docker

Runs an SSH server, serving gitolite as the git@ user.

On the first start, it will run "gitolite setup" with a starting ssh key
you provided, or you can bootstrap with an existing gitolite-admin repository.

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

**TRUST_HOSTS**

Hostnames (only a single one is supported currently) to add to known_hosts, i.e. *github.com*.

### Directories you could bind mount (or use --volumes-from)

/home/git/repositories
  The actual git repositories will be stored here.

/etc/ssh
  The SSH host keys are stored here; they are generated when the container starts,
  and if you don't maintain them across containers, your clients will see warnings
  that they changed.

### Mirroring

If your gitolite install needs to mirror (that is, execute git push itself), the
image can help you:

* The git user will have a ssh key generated for itself. Access the public  key using
  *docker cp CID:/home/git/.ssh/id_rsa.pub .*.

  Note that if you keep recreating the container, rather than restarting, a new key
  will be generated. You can bind mount the **/home/git/.ssh** directory to
  remedy this.

* Use the *TRUST_HOSTS* environment variable to prepare the ./known_hosts file.

## Further customization

If you need to use things like custom hooks, you have different options:

* Point the *LOCAL_CODE* variable to something like "$ENV{HOME}/.gitolite/local", use the gitolite-admin repo to provide the data.
* You could bind mount files into the container (xxx: how to provide certain files (gitolite.rc) before setup runs?)
* Derive a custom Docker image, ADD the files (xxx: how to provide certain files (gitolite.rc) before setup runs?)
* Manually interact with a container, but lose it disposible nature.
