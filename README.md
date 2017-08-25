# IOI Printing system

IOI Printing system is the system used to handle all print requests in [International Olympiad in Informatics](http://www.ioinformatics.org/) during contest and in translation meetings.
It has been developed and used first in [29th IOI](http://ioi2017.org/) in Tehran, Iran.

The current system supports the following tasks and requests:
  * Print requests from contestants during contest (By a custom printer installed on all contestants pc) \[`contestant`\]
  * Call staff requests from [IOI Contest Management System](https://github.com/akmohtashami/cms) \[`cms_request`\]
  * Custom translation print requests used during translation meetings from [IOI Translation System](https://github.com/noidsirius/IOI-Translation) \[`translation`\]
  * Custom print requests \[`mass`\]

It also connects to [IOI Net Administraion System](https://github.com/m30m/net-admin) to get contestant information during contests.

## Installation

To run this project you need to install [docker](https://docs.docker.com/engine/installation/) and [docker-compose](https://docs.docker.com/compose/install/).
(It has been deployed and tested with docker 17.06.0-ce and docker-compose 1.14.0 but it must work with the latest versions too.)

All you need to do is to make sure everything is configured correctly in `docker-compose.yml` (descriptions on how to configure is written as comments in the file) and run:

```bash
docker-compose up
```

(You might get into errors if cups server is running or if something else using 631, 5000 or 6631 ports)

For running on actual server you might want to run docker-compose in daemon mode:

```bash
docker-compose up -d
```

Check out [docker-compose documentation](https://docs.docker.com/compose/) for more info.

## How to use

#### Configure printers

Go to `http://printer_server_address:6631/`, it is cups server configuration page.
Add your printers there (You can also add classes to assign a single name to multiple printers).
Then put your printers' names in `docker-compose.yml` (You can have a printer for each contest zone and also one default printer for `mass` and `translation` requests)

#### For contestants print requests

You should add a network printer with the address `ipp://print_server_address:631/printers/ioi_printer` on all contestants' computers.
([This link](http://smallbusiness.chron.com/add-network-printer-linux-57531.html) can be helpful)

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

## Service Details

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

## cups-front

A cups server running on port 631 (You can change it in `docker-compose.yml`).

This cups server exposes a printer named `ioi_printer`, whenever a print request is received on this printer it would call `upload` and `contestant` on `ioiprint` to do the actual printing.
The printer is a `cups-pdf` pdf printer and a cups filter named `ioi-filter` is used to do this.
(You can check the code in `cups` directory)

## cups-back

A cups server running on port 6631 (You can change it in `docker-compose.yml`).

This cup server is the one that all printers are configured on and the actual printings are happening here.
All print requests from `ioiprint` comes to this cups server.
