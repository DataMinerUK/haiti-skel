Matplotlib Haiti
================
Example `skel` data driven journalism project using Ushahidi example from
Python for Data Analysis Chapter 8 by Wes McKinney.

Data
----
* Ushahidi Haiti earthquake dataset from: http://community.ushahidi.com/research/datasets
* Port-au-prince shapefiles from Harvard and OpenStreetMaps.

Steps
-----
* Install [VirtualBox][virtualbox]
* Install [Vagrant][vagrant]. See `README.vagrant.md` for instructions.

Then to recreate the output files in `out`:

    $ vagrant up
    $ vagrant ssh
    Welcome to Ubuntu 12.04 LTS (GNU/Linux 3.2.0-23-generic x86_64)

	 * Documentation:  https://help.ubuntu.com/
	Welcome to your Vagrant-built virtual machine.
	Last login: Sun Nov 25 17:13:15 2012 from 10.0.2.2
	> cd /vagrant
	> ./run.sh
	> exit

The cleaned data files and output plot PDFs will have been recreated in `out`.

[virtualbox]: https://www.virtualbox.org/wiki/Downloads
[vagrant]: http://vagrantup.com
[sequel]: http://www.sequelpro.com/
[XQuartz]: http://xquartz.macosforge.org/