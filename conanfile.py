from conans import ConanFile, CMake, tools
import os

class BlazeConan(ConanFile):
    name = "blaze"
    version = "3.0"
    branch = "stable"
    license = "BSD"
    generators = "cmake"
    url = 'http://github.com/wrayste/conan-blaze'
    gz_file_sha = "d66abaf4633d60b6e6472f6ecd7db7b4fb5f74a4afcfdf00c92e1ea61f2e0870"

    def source(self):
        gz_name = "blaze-%s.tar.gz" % (self.version)
        url = 'https://bitbucket.org/blaze-lib/blaze/downloads/%s' % (gz_name)
        tools.download(url, gz_name)
        tools.check_sha256(gz_name, self.gz_file_sha)
        tools.unzip(gz_name)
        os.unlink(gz_name)

    def package(self):
        self.copy(pattern="*", dst="include/blaze", src="blaze-%s/blaze" % self.version)
