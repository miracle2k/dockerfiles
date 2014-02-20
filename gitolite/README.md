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

Will be inserted into gitolite.rc.

### Directories you may bind mount.

/home/git/repositories
  The actual git repositories will be stored here.
