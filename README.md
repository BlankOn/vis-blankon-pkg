BlankOn Repository - Total Packages and Sizes
============================================

This Git repository contains scripts I use to gather and visualize the Ubuntu
repositories in terms of total packages and their total size.

Check the GitHub page for the result - <http://arsip.blankonlinux.or.id/>.

How?
----

I took the package index files (a.k.a. `Packages` file) and counted the number
of packages inside. I also summed the size of each packages to get the size of
the repository. The files are from the "at-release" repository which means I
excluded the `-updates` and `-security` repositories. The at-release repository
is presumably frozen and therefore the size won’t change anymore, where the
latest two repositories are for the updates, which by definition are always
updated.  Well.. except when the release is not supported anymore.


How To Run?
-----------

First, adjust the list of repositories, archive urls, etc in the `config.py` file.

    $ vi config.py

Then, download all index files

    $ python download.py data/

The files will be downloaded into the given data directory. In the above
example, the data directory is `data/`.

After that, run the analysis script to collect all numbers from the index
files. Put the result into a file so we don't need to do this again.

    $ python analyze.py data/ > out/raw-data.json

Once it's ready, run the visualization script to create codes needed to make
charts using Google Chart API.

    $ python visualize.py out/raw-data.json > out/data.js

Finally, open the HTML page I made to show the data.

    $ xdg-open index.html

