# Running with systemd

1. As root, enable lingering user units:

   ```sh
   loginctl enable-linger <username>
   ```

2. Copy file to `~/.config/systemd/user.control/`

   These commands shall be run form the root of the repository.

   ```sh
   mkdir -p ~/.config/systemd/user.control
   cp systemd/sharp-remote.service ~/.config/systemd/user.control/
   ```

3. Enable and start the unit

   ```sh
   systemctl --user daemon-reload
   systemctl --user enable sharp-remote
   systemctl --user start sharp-remote
   systemctl --user status sharp-remote
   ```
