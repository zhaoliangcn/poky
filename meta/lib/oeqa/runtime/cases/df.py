#
# Copyright OpenEmbedded Contributors
#
# SPDX-License-Identifier: MIT
#

from oeqa.runtime.case import OERuntimeTestCase
from oeqa.core.decorator.depends import OETestDepends
from oeqa.core.decorator.data import skipIfDataVar, skipIfInDataVar
from oeqa.runtime.decorator.package import OEHasPackage

class DfTest(OERuntimeTestCase):

    @OETestDepends(['ssh.SSHTest.test_ssh'])
    @OEHasPackage(['coreutils', 'busybox'])
    @skipIfInDataVar('IMAGE_FEATURES', 'read-only-rootfs', 'Test case df requires a writable rootfs')
    def test_df(self):
        cmd = "df -P / | sed -n '2p' | awk '{print $4}'"
        (status,output) = self.target.run(cmd)
        msg = 'Not enough space on image. Current size is %s' % output
        self.assertTrue(int(output)>5120, msg=msg)
