# IOI Print system


## TODO

- Global scope
    - [x] Check PDF Creation in Server

- Constestant print request
    - [x] First and last page templates
    - [ ] Front CUPS - configure `ioi-printer`
    - [ ] Create classes
    - [ ] Check if constestant computers can see `ioi-printer`
    - [ ] Get contestant data
        - for each IP: ID, Name, Country, Location, Floor
        - for each Location: SVG image

- CMS Request
    - [ ] Determine types of requests (farzad)
    - [ ] Template
    - [x] Bash script in CMS - request_type:String, IP (farzad)
    - [ ] Bash script in Print server

- Translation
    - [ ] Translation Printer Class
    - [ ] First page template
    - [x] Bash script in Translation system - Input Arguments: file_path, country_code, country_name, [count]
    - [ ] Bash script in Print server

- Mass Print Command
    - [x] Bash script - Input Arguments: file_path, count, printer/class


## `ioiprint` python script
Resides in (front-) print server

Arguments:
- `ioiprint translation file_path country_code country_name count`
- `ioiprint cms request_msg ip`
- `ioiprint contestant file_path ip`
- `ioiprint mass file_path printer count`
