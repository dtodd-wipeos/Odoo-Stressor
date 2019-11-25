# Odoo Stressor

This collection of scripts provides an XMLRPC API to Odoo (versions 9-13)
to fulfill its primary purpose, which is to cause a significant load on the system.

The goal of stress testing is to ensure that the target service is properly configured
to utilize all of the available resources and to not cause significant denial of service under heavy load

Currently, the only availabe stress option is performing heavy searches on models known to have a lot of rows.
More may be added in the future

## Requirements

Everything is part of the python3 standard library, go nuts!

## Usage

There are multiple ways that this program can be used, but ultimately they both do the same thing.
The first is to edit the `run.sh` script with the parameters that you want, and then run it.
The second is to export the following into your envirnoment before running `stressor.py`

* `export odoo_host='<string, required, the hostname of your odoo instance>'` - Include the `http(s)://` at the beginning
* `export odoo_database=<string, required, the database you are interacting with>`
* `export odoo_user=<integer, optional, your user's database id>` - The default value of 1 for the `admin` user will be used if not provided
* `export odoo_pass='<string, required, your user's password>'`
* `export stress_threads=<integer, optional>` - The default value of 100 will be used if not provided
* `export stress_loops=<integer, optional>` - The default value of 1000 will be used if not provided
* `export wait_time=<integer, optional>` - The default value of 30 will be used if not provided. Defines how long the script will wait between each `stress_loop`

These will be loaded in by the stressor and then ran by creating a bunch of threads, each selecting a random model and stress method.
Then it will do it again for however many `stress_loops` are defined.

### Docker

There is now a docker file for large scale stress testing.
The container that this creates is about 60.5MiB in size, much smaller than Debian's official `buster slim python` container.

`build-run-docker.sh` is a convenience mechanism that will create a minimal docker container and run it (essentially the same as running the script yourself)

If you are going to use docker, be sure to create a `.env` file with the same layout as `sample.env` before running `build-run-docker.sh`

#### `.env` file

The .env file must not contain quotes around any of the arguements, else you will get invalid contexts with `XMLRPC`.
The variables are defined just like the ones required if you were to use `run.sh`

## MIT License

Copyright 2019 David Todd <dtodd@oceantech.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
