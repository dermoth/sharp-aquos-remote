# Sharp AQUOS Web Remote

I have a nice Sharp AQUOS TV installed in an easel that blocks the IR sensor.
There's a web interface I used to connect to and control, so I wrote a web app
to make it easier and allow family to control the TV as well.

The app runs very well from a smartphone browser, although WebKit seems to be
taking a long time to render the SVG (this affects Safari and even Chrome under
iOS as they're forced to use WebKit, other browsers I've tested render quickly
and flawlessly).

## Install

Since I wrote it I haven't had much tine to document it, so feel free to open a
ticket to request more documentation if you need it. Make sure your specific TV
model support this type of remote control as this project won't support other
models, or at least I won't be the author of that.

Requests to implement support to non-AQUOS TV's will likely be ignored.

## Known issues

* Remote image is too big on desktop browsers; need to limit size (users can
  zoom down in the meantime)
* Power button does't not turn on the TV (need to send the `POWR 1___` command)
* On network issues, commands may backlog and run all at once
* API is likely vulnerable to CSRF attacks or similar

## TODO

* I wanted to add a tab for direct control that would allow that, ex setting
  volume at a specific level, and any other useful commands
* Add a command to configure the remote control (ex. enable/disable always-on
  mode)

## License

Copyright (C) 2023-2024 Thomas Guyot-Sionnest <tguyot@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
