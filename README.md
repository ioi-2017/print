### IOI Print system


## TODO

- Global scope
    - [ ] Check PDF Creation in Server

- Constestant print request
    - [x] First and last page templates
    - [ ] Front CUPS - configure `ioi-printer`
    - [ ] Create classes
    - [ ] Check if constestant computers can see `ioi-printer`
    - [ ] Get contestant data
        - for each IP: ID, Name, Country, Location, Floor
        - for each Location: SVG image

- CMS Request
    - [ ] Determine types of requests
    - [ ] Template
    - [ ] Bash script in CMS - request type, IP
    - [ ] Bash script in Print server

- Translation
    - [ ] Translation Printer Class
    - [ ] First page template
    - [ ] Bash script in Translation system - Input Arguments: file path, country code, country name
    - [ ] Bash script in Print server

- Mass Print Command
    - [ ] Bash script - Input Arguments: file path, count, printer/class
