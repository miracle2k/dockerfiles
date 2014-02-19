# I find myself repeating the same code over and over, maybe this will help.
set -e

die () {
    echo >&2 "$@"
    exit 1
}

# Create a directory, and copy the contents of another directory there, *only* if
# the target directory did exist yet (i.e. on first start).
init_directory () {
    [ -n "$1" ] || die "need at least one argument, the directory to create"
    dir=$1

    if [ -d "$dir" ]; then
        echo "$dir already initialized, leaving alone"
        return
    else
        mkdir -p "$dir"
        if [ -n "$1" ]; then
            echo "Copying $1 to $dir"
            cp -r $2/* "$dir"
        fi
    fi
}
