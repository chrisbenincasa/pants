# coding=utf-8
# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import absolute_import, division, print_function, unicode_literals

from contextlib import contextmanager

import mock

from pants.pantsd.watchman_client import StreamableWatchmanClient
from pants_test.test_base import TestBase


class TestWatchmanClient(TestBase):
  def setUp(self):
    super(TestWatchmanClient, self).setUp()
    self.swc = StreamableWatchmanClient(sockpath='/tmp/testing', transport='local')

  @contextmanager
  def setup_stream_query(self):
    with mock.patch.object(StreamableWatchmanClient, '_connect') as mock_connect, \
         mock.patch.object(StreamableWatchmanClient, 'sendConn') as mock_sendconn, \
         mock.patch.object(StreamableWatchmanClient, 'recvConn') as mock_recvconn:
      yield mock_connect, mock_sendconn, mock_recvconn

  def test_stream_query(self):
    with self.setup_stream_query():
      self.swc.stream_query([])
