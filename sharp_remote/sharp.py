"""Sharp Remote Controller"""

import logging
import socket
import select
from errno import EPIPE, ENOTCONN

log = logging.getLogger('TvController')

class TvControllerError(Exception):
    """Generic TvController error
    """
class TvControllerCmdFormatError(TvControllerError):
    """TvController Command Format error
    """

class TvController:
    """TV Controller Class"""
    def __init__(self, host=None, port=10002, devicename=None, close=True):
        """TvController holds the connection to the TV and allows sending
        commands to ité

        Args:
            hostname (str, optional): Host/IP to connect to.
            port (int, optional): Port to connect to. Defaults to 10002.
            devicename (str, optional): Connect using ssdp, look for this name.
            close (bool, optional): close connections after every command
        """

        if devicename:
            raise TvControllerError('SSDP lookup is not implemented yet')

        if devicename and host:
            # Should we validate both match? I would just ignore the devicename...
            log.info('Ignoring devicename as a hostname was provided')

        self._host = host
        self._port = port
        self._sock = self.newsock()

        # This could eventually be determined from the TV model...
        self.remote = 'GB005WJSA'
        self.name = devicename if devicename else 'TODO: set name'
        self.close = close

    @staticmethod
    def newsock():
        """Create a new socket"""
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def shutdown(self):
        """Shutdown and create new socket"""
        self._sock.shutdown(socket.SHUT_RDWR)
        self._sock.close()
        self._sock = self.newsock()

    @property
    def sock(self):
        """Connect to the socket and return it

        Returns:
            socket: Connected socket
        """
        try:
            self._sock.getpeername()
            self._sock.send(b'')
        except OSError as err:
            if err.errno == EPIPE:
                log.warning('Connection from %s:%i lost, reconnecting...', self._host, self._port)
                self.shutdown()
            if err.errno in (EPIPE, ENOTCONN):
                log.info('Connecting to %s:%i', self._host, self._port)
                self._sock.connect((self._host, self._port))
        return self._sock

    def send(self, msg):
        """Send message to TV

        Args:
            msg (bytes): Data to send

        Raises:
            TvControllerError: Failed to connect or sent msg
        """
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise TvControllerError('Failed writing to socket')
            totalsent = totalsent + sent

    def recv(self, timeout=5):
        """Read result from TV

        Args:
            timeout (int, optional): Wait delay for command results. Defaults to 5.

        Raises:
            TvControllerError: Connection error

        Returns:
            str: Result from TV
        """
        chunks = []
        # FIXME: Unless there's python magic we need to keep track of time until timeout is elapsed
        while select.select((self.sock,), (), (), timeout)[0]:
            chunk = self.sock.recv(1)
            if chunk == b'':
                raise TvControllerError('Socket connection broken')
            chunks.append(chunk)
            if chunk == b'\r':
                break
        return b''.join(chunks)

    def command(self, cmd, arg):
        """Send a command to the TV

        Args:
            cmd (str): 4-character command
            arg (str): 1-4 character argument

        Returns:
            bool or str: Command result (very few commands return a string)
        """
        if not isinstance(cmd, str) or len(cmd) != 4:
            raise TvControllerCmdFormatError(f"Command {cmd} not a 4-char string")

        if not isinstance(arg, str) or arg == '' or len(arg) > 4:
            raise TvControllerCmdFormatError(f"Argument {arg} not a 1 to 4-char string")
        arg += ' ' * (4 - len(arg))

        tvcmd = cmd + arg + '\r'
        self.send(tvcmd.encode('UTF-8'))

        while 1:
            resp = self.recv().decode('UTF-8')
            log.info('received %s', resp.strip('\r'))
            if resp == '' or resp[0:3] != 'ERR':
                break

        if self.close:
            self.shutdown()
        return True
