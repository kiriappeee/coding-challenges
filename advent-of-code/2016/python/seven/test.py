import unittest
from seven import ex

class Test20160701(unittest.TestCase):
    def test_abba_string_can_be_identified(self):
        self.assertTrue(ex.is_abba("abba"))
        self.assertFalse(ex.is_abba("axxj"))
        self.assertTrue(ex.is_abba("aabba"))
        self.assertTrue(ex.is_abba("ioxxoj"))
        self.assertFalse(ex.is_abba("zxcvbn"))
        self.assertFalse(ex.is_abba("aaa"))
        self.assertTrue(ex.is_abba("aoxxiix"))

    def test_ip_can_be_broken_down(self):
        self.assertEqual(ex.break_down_ip("abba[mnop]qrst"), {"nonhypernet": ["abba", "qrst"], "hypernet": ["mnop"]})
        self.assertEqual(ex.break_down_ip("ioxxoj[asdfgh]zxcvbn"), {"nonhypernet": ["ioxxoj", "zxcvbn"], "hypernet": ["asdfgh"]})
        self.assertEqual(ex.break_down_ip("ioxxoj[asdfgh]asdasdas[something]zxcvbn"), {"nonhypernet": ["ioxxoj", "asdasdas", "zxcvbn"],  "hypernet": ["asdfgh", "something"]})
        self.assertEqual(ex.break_down_ip("rnqfzoisbqxbdlkgfh[lwlybvcsiupwnsyiljz]kmbgyaptjcsvwcltrdx[ntrpwgkrfeljpye]jxjdlgtntpljxaojufe"), {"nonhypernet": ["rnqfzoisbqxbdlkgfh", "kmbgyaptjcsvwcltrdx", "jxjdlgtntpljxaojufe"], "hypernet": ["lwlybvcsiupwnsyiljz", "ntrpwgkrfeljpye"]})

    def test_ip_is_tld_can_be_identified(self):
        self.assertTrue(ex.is_tls("abba[mnop]qrst"))
        self.assertFalse(ex.is_tls("abcd[bddb]xyyx"))
        self.assertFalse(ex.is_tls("aaaa[qwer]tyui"))
        self.assertTrue(ex.is_tls("ioxxoj[asdfgh]zxcvbn"))

class Test20160702(unittest.TestCase):
    def test_aba_strings_can_be_found(self):
        self.assertEqual(ex.find_aba("aba"), ["aba"])
        self.assertEqual(ex.find_aba("zazbz"), ["zaz", "zbz"])
        self.assertEqual(ex.find_aba("abazazbz"), ["aba", "aza", "zaz", "zbz"])

    def test_reverse_aba_string_is_identified(self):
        self.assertTrue(ex.bab_exists(["aba", "aza", "zaz"], ["axx", "aza"]))
        self.assertTrue(ex.bab_exists(["aba"], ["chasdkjebabjklhasdlkj"]))
        self.assertFalse(ex.bab_exists(["xyx"], ["chasdkjebabjklhasdlkj"]))

    def test_ip_is_sls_can_be_identified(self):
        self.assertTrue(ex.supports_sls("aba[bab]xyz"))
        self.assertFalse(ex.supports_sls("xyx[xyx]xyx"))
        self.assertTrue(ex.supports_sls("aba[bab]xyz"))
        self.assertTrue(ex.supports_sls("aba[bab]xyz"))
        self.assertTrue(ex.supports_sls("jhasfulhyeabalkjasdnzuznz[jkhuihr]jlhkjsahdfwewjbzx[jhfdsuhuihasdanznasdklja]lkajsduhqbcb"))
if __name__ == "__main__":
    unittest.main()
