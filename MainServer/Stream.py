import mimetypes
import os
import re
from config import Config
from flask import Response


class Stream:
    def __init__(self, logger):
        self.logger = logger

    @staticmethod
    def StreamGen(frame):
        yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'

    def GetRange(self, request):
        range_require = request.headers.get('Range')
        self.logger.info('Requested: %s', range_require)
        m = re.match("bytes=(?P<start>\d+)-(?P<end>\d+)?", range_require)
        if m:
            start = m.group('start')
            end = m.group('end')
            start = int(start)
            if end is not None:
                end = int(end)
            return start, end
        else:
            return 0, None

    def PartialResponse(self, path, start, end=None):
        self.logger.info('Requested: %s, %s', start, end)
        file_size = os.path.getsize(path)

        # Determine (end, length)
        if end is None:
            end = start + Config.BufferSize - 1
        end = min(end, file_size - 1)
        end = min(end, start + Config.BufferSize - 1)
        length = end - start + 1

        # Read file
        with open(path, 'rb') as fd:
            fd.seek(start)
            byte_data = fd.read(length)
        assert len(byte_data) == length

        response = Response(
            byte_data,
            206,
            mimetype=mimetypes.guess_type(path)[0],
            direct_passthrough=True,
        )
        response.headers.add(
            'Content-Range', 'bytes {0}-{1}/{2}'.format(
                start, end, file_size,
            ),
        )
        response.headers.add(
            'Accept-Ranges', 'bytes'
        )
        self.logger.info('Response: %s', response)
        self.logger.info('Response: %s', response.headers)
        return response
