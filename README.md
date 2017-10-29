IOI Printing System
===================

The IOI Printing System handles all print requests in the International
Olympiad in Informatics, during the contests and the translation meetings.
The system has been developed for and was first used in the
[IOI 2017](http://ioi2017.org/) in Tehran, Iran.

The system supports the following tasks and requests:
  * Print requests from contestants during the contest
    (via a custom printer installed on all contestants machines) [`contestant`]
  * Call staff requests from the IOI Contest Management System [`cms_request`]
  * Print requests from the IOI Translation System during the translation meetings
    [`translation`]
  * Custom mass print requests [`mass`]


Installation
------------

To run the project, you need to install
[docker](https://docs.docker.com/engine/installation/) and
[docker-compose](https://docs.docker.com/compose/install/).
(It has been deployed and tested with docker 17.06.0-ce
and docker-compose 1.14.0, but it should work with newer versions as well.)

After that, clone the project using the following command:

```bash
git clone git_address/print-system.git
```

Then configure the project in `docker-compose.yml`
(descriptions on how to configure is commented in the file), and run:

```bash
docker-compose up
```

(You might get into errors if cups server is running or if someone else
is using ports 631, 5000, or 6631.)

That's it! You have the printing system up and ready for work!

For running on actual server you might want to run docker-compose in daemon mode:

```bash
docker-compose up -d
```

Check out [docker-compose documentation](https://docs.docker.com/compose/) for more info.

How to Use
----------

#### Configure printers

Go to `http://printer_server_address:6631/`, it is cups server configuration page:
1. Go to `Administration page`, login with predefined username `admin` and password `ioi`.
2. Click on `Add Printer`, select `Internet Printing Protocol (ipp)`, click `Continue`.
3. Write the network printer address in `Connection`, click `Continue`. (Check your printer manual to find its ipp address)
4. Set a `Name` for your printer and make sure `Share This Printer` is selected, click `Continue`. (The `Name` you use for your printer are the ones that you use in configuring printers in `ioiprint` in `docker-compose.yml`)
5. Select `Generic` in the `Make` section, click `Continue`.
6. Select `Generic IPP Everywhere Printer (en)` in the `Model` section, click `Continue`.
7. Set default options for your printer, click `Set default options`.
8. Play a little with printer default options and make sure print requests are handled correctly in the printer.
You can use `Maitenance` -> `Print Test Page` in the printer page to test printing.

You can also add classes to assign a single name to multiple printers:
1. Go to `Administration page`, click on `Add Class`.
2. Set a `Name` for your class and select printers you want in the `Members` section, click `Continue`. (The `Name` you use for your class are the ones that you use in configuring printers in `ioiprint` in `docker-compose.yml`)

Then put your printer or class names in `docker-compose.yml` (You can have a printer for each contest zone and also one default printer for `mass` and `translation` requests)

#### For contestants print requests

You should add a network printer with the address `http://print_server_address:631/printers/PRINTER_NAME` on all contestants' computers.
([This link](http://smallbusiness.chron.com/add-network-printer-linux-57531.html) can be helpful)
PRINTER_NAME is configurable in `docker-compose.yml`. (It is `ioi_printer` by default)

The contestants can print using this printer during contest and it will be printed on the printer configured for that zone.

You can also change the templates used for rendering the first page and the last page of the prints by changing the `first.html.jinja2` and `last.html.jinja2` in `ioiprint/template` directory (They are in [Jinja2](http://jinja.pocoo.org/) format).

#### For call staff requests from CMS

You should add print server address in [CMS](https://github.com/akmohtashami/cms) and it should work.

For testing you can use `scripts/cms_request.sh` (You should change `PRINT_SERVER_ADDRESS`).

You can also change the template used for rendering the prints by changing the `request.html.jinja2` in `ioiprint/template` directory (They are in [Jinja2](http://jinja.pocoo.org/) format).

#### For custom translation requests from Translation System

You should add print server address in [Translation System](https://github.com/noidsirius/IOI-Translation) and it should work.

For testing you can use `scripts/translation.sh` (You should change `PRINT_SERVER_ADDRESS`).

(Translation System also uses the `mass` request for non-custom prints.)

You can also change the template used for rendering the prints by changing the `translation.html.jinja2` in `ioiprint/template` directory (They are in [Jinja2](http://jinja.pocoo.org/) format).

#### For custom printing

You can use `scripts/mass.sh` (You should change `PRINT_SERVER_ADDRESS`).

Service Details
---------------

This service is consisted of three docker containers that are explained in details below:

#### ioiprint

An http server running on port 5000 (you can change it in `docker-compose.yml`).

There are 5 type of requests system can handle:

###### upload

```
endpoint: /upload
method: POST
parameters: pdf -> a pdf file in multi-part form data
output: uploaded_file_name -> Used in other requests
```

You should upload a pdf file before using `mass`, `contestant` or `translation` requests.
This endpoint is used to upload files and it will give back the file name in the response body.
You should use this file name in the next request.

###### mass

```
endpoint: /mass
method: POST
parameters: filename -> output of previously called upload request
            printer -> printer or class name that is configured in cups-back server
                       (If not given default printer is used)
            count -> number of times the system should print the file
```

This will print the file previously uploaded `count` times on the printer specified.

###### translation

```
endpoint: /translation
method: POST
parameters: filename -> output of previously called upload request
            country_code -> country code of the translating country (e.g. IR)
            country_name -> country name of the translating country (e.g. Iran)
            count -> number of times the system should print the file
```

This will add a first page and print the file previously uploaded `count` times on default printer.

###### cms_request

```
endpoint: /cms_request
method: POST
parameters: request_message -> The request message (e.g. Restroom)
            ip -> IP of the contestant computer
```

This will print a page with contestant info and request message on the printer configured for the contestant zone.

###### contestant

```
endpoint: /contestant
method: POST
parameters: filename -> output of previously called upload request
            ip -> IP of the contestant computer
            cups_job_id -> The print job id of the cups server requesting this print
```

This will add a first and last page to the file and print it on the printer configured for the contestant zone.
(This endpoint is automatically called from cups-front)

#### cups-front

A cups server running on port 631 (You can change it in `docker-compose.yml`).

This cups server exposes a printer named `ioi_printer`, whenever a print request is received on this printer it would call `upload` and `contestant` on `ioiprint` to do the actual printing.
The printer is a `cups-pdf` pdf printer and a cups filter named `ioi-filter` is used to do this.
(You can check the code in `cups` directory)

#### cups-back

A cups server running on port 6631 (You can change it in `docker-compose.yml`).

This cup server is the one that all printers are configured on and the actual printings are happening here.
All print requests from `ioiprint` comes to this cups server.

Changing Contestant Data Source
-------------------------------

By default the system will get contestant data from the IOI Network Administration System,
and the address is configurable in `docker-compose.yml`.

If you want to change the source of contestant data (e.g. to read it from a file)
you should change the `get_contestant_data` function in `ioiprint/contestant_data.py` file.
The input of the function is the ip of the contestant's computer.
The output should be a python dictionary consisting of the following keys:
- `contestant_id`: ID of the contestant
- `contestant_name`: Name of the contestant
- `contestant_country`: Country name of the contestant
- `zone`: Zone that contestant sits in (It is used for determining which printer should we use for this contestant)
- `desk_id`: ID of the contestant's desk
- `desk_image_url` or `desk_image_path`: The SVG image of the map showing where the contestant is sitting.
It will be downloaded if you provide `desk_image_url` or you should use `desk_image_path` if the file is on the computer already.
(Please note that the path should be a path inside the docker container. e.g. `/usr/src/ioiprint/svgs/contestant1.svg`)

License
-------

This software is distributed under the MIT license (see LICENSE.txt),
and uses third party libraries that are distributed under their own terms
(see LICENSE-3RD-PARTY.txt).

Copyright
---------
Copyright (c) 2017, IOI 2017 Host Technical Committee
